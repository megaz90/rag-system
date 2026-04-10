from src.core.config import LLM_PROVIDER
from src.core.llm.base import BaseLLMChatModel
from src.core.llm.llm_chat_models import OllamaChatModel, OpenAIChatModel


def llm_provider(**kwargs) -> BaseLLMChatModel:
    """
    Factory function that instantiates and returns an LLM provider based on the configured provider name.

    Additional keyword arguments are forwarded to the underlying provider class constructor, allowing flexible
    configuration (e.g., system prompts, API settings, etc.).
    """
    provider = LLM_PROVIDER.lower()

    if provider == "ollama":
        return OllamaChatModel(**kwargs)

    if provider == "openai":
        return OpenAIChatModel(**kwargs)

    raise ValueError(f"Unknown provider: {provider}")
