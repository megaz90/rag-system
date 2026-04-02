from pathlib import Path
from typing import Any, Dict

import chromadb
from chromadb.api.models.Collection import Collection
from chromadb.api.types import QueryResult
from sentence_transformers import SentenceTransformer

from .config import COLLECTION_NAME, EMBEDDINGS_MODEL


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

        self.embedding_model = SentenceTransformer(EMBEDDINGS_MODEL)
        self.chroma_client = chromadb.PersistentClient(
            path=str(BASE_DIR / "data/chroma_db")
        )

    def get_or_create_collection(self) -> Collection:
        """Retrieve existing collection or create it if it doesn't exist."""
        return self.chroma_client.get_or_create_collection(name=COLLECTION_NAME)
    
    def search_database(self, query: str, top_result: int = 3) -> QueryResult:
        """
        Retrieve the most similar document chunks from the vector database.

        Steps:
        - Convert query into embedding
        - Query ChromaDB using cosine similarity
        - Return top matching chunks
        """
        query_embeddings = db.embedding_model.encode([query])[0].tolist()
        collection = db.get_or_create_collection()

        return collection.query(query_embeddings=query_embeddings, n_results=top_result)


db = VectorDatabase()
