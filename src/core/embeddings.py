from sentence_transformers import SentenceTransformer

from .config import EMBEDDINGS_MODEL


class VectorEmbedding:
    """
    Singleton class for vector embeddings.
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        """
        Ensures only one instance of VectorEmbedding exists.

        If an instance already exists, return it instead of creating a new one.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.embedding_model = SentenceTransformer(EMBEDDINGS_MODEL)
