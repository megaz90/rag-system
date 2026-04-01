import chromadb
from sentence_transformers import SentenceTransformer

from .config import EMBEDDINGS_MODEL


class VectorDatabase:
    _instance = None
    _initialized = False

    # Singleton so that it is not instantiated each time it is called.
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self.embedding_model = SentenceTransformer(EMBEDDINGS_MODEL)

        self.chroma_client = chromadb.Client()


db = VectorDatabase()
