import os

from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("OLLAMA_LLM_MODEL", "qwen3.5:0.8b")

EMBEDDINGS_MODEL = os.getenv("HF_EMBEDDINGS_MODEL", "all-MiniLM-L6-v2")

COLLECTION_NAME = os.getenv("COLLECTION_NAME", "rag_collection")

LLM_PROVIDER = str(os.getenv("LLM_PROVIDER"))

# Default Prompts for LLM
SYSTEM_PROMPT = """You are a helpful assistant that answers questions based on the provided context."""
