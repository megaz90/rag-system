from pathlib import Path
from typing import cast

import chromadb
from chromadb.api.models.Collection import Collection
from chromadb.api.types import QueryResult, Where

from src.core.embeddings import vector_embedding
from src.schemas.query_context import QueryContext

from .config import COLLECTION_NAME


class VectorDatabase:
    """
    Singleton Vector Database manager.

    Responsibilities:
    - Initialize embedding model once
    - Initialize persistent ChromaDB client once
    - Provide access to collections
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        """
        Ensures only one instance of VectorDatabase exists.

        If an instance already exists, return it instead of creating a new one.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        BASE_DIR = Path(__file__).resolve().parents[2]

        self.chroma_client = chromadb.PersistentClient(
            path=str(BASE_DIR / "data/chroma_db")
        )

    def _normalize_results(self, results: QueryResult) -> list[dict]:
        """Normalize ChromaDB query results into a list of dictionaries."""

        documents = results.get("documents") or []
        metadatas = results.get("metadatas") or []
        ids = results.get("ids") or []
        distances = results.get("distances") or []

        # Chroma returns nested lists
        if documents and isinstance(documents[0], list):
            documents = documents[0]
            metadatas = metadatas[0] if metadatas else []
            ids = ids[0] if ids else []
            distances = distances[0] if distances else []

        normalized = []

        for i, doc in enumerate(documents):
            normalized.append(
                {
                    "id": ids[i] if i < len(ids) else None,
                    "text": doc,
                    "metadata": metadatas[i] if i < len(metadatas) else {},
                    "score": distances[i] if i < len(distances) else None,
                }
            )

        return normalized

    def get_or_create_collection(self) -> Collection:
        """Retrieve existing collection or create it if it doesn't exist."""
        return self.chroma_client.get_or_create_collection(name=COLLECTION_NAME)

    def search_database(self, context: QueryContext, top_result: int = 3) -> list[dict]:
        """
        Retrieve the most similar document chunks from the vector database.

        Steps:
        - Convert query into embedding
        - Query ChromaDB using cosine similarity
        - Return top matching chunks
        """
        if context.rewritten_query is None:
            query_embeddings = vector_embedding.embedding_model.encode([context.query])[
                0
            ].tolist()
        else:
            query_embeddings = vector_embedding.embedding_model.encode(
                [context.rewritten_query]
            )[0].tolist()

        collection = self.get_or_create_collection()

        where = (
            cast(Where, {"category": {"$in": context.sources}})
            if context.sources
            else None
        )
        results = collection.query(
            query_embeddings=query_embeddings, n_results=top_result, where=where
        )
        return self._normalize_results(results)


db = VectorDatabase()
