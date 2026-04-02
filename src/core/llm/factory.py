from src.core.config import LLM_PROVIDER
from src.core.llm.llm_chat_models import OllamaChatModel, OpenAIChatModel


def llm_provider():
    provider = LLM_PROVIDER.lower()

    if provider == "ollama":
        return OllamaChatModel()

    if provider == "openai":
        return OpenAIChatModel()

    raise ValueError(f"Unknown provider: {provider}")
