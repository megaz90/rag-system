from pathlib import Path

import chromadb
from chromadb.api.models.Collection import Collection
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


db = VectorDatabase()
