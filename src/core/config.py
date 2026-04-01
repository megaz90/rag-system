import os

from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("OLLAMA_LLM_MODEL", "qwen3.5:0.8b")

EMBEDDINGS_MODEL = os.getenv("HF_EMBEDDINGS_MODEL", "all-MiniLM-L6-v2")
