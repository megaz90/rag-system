from ollama import ChatResponse, chat

from src.core.config import MODEL_NAME, SYSTEM_PROMPT


class OllamaChatModel:
    """
    Wrapper for ollama chat model
    """

    def __init__(self, system_content: str = SYSTEM_PROMPT):
        self.system_content = system_content

    def build_messages(self, user_content: str):
        return [
            {"role": "system", "content": self.system_content},
            {"role": "user", "content": user_content},
        ]

    def generate(self, prompt: str) -> ChatResponse:
        """
        TODO: Add a normalizer function to normalize the response
        """
        messages = self.build_messages(prompt)
        try:
            return chat(
                model=MODEL_NAME,
                messages=messages,
            )

        except Exception as e:
            raise RuntimeError(f"LLM generation failed: {e}")


class OpenAIChatModel:
    """
    TODO: Add OpenAIChatModel
    """

    pass
