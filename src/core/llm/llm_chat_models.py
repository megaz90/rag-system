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
        message = self.build_messages(prompt)

        return chat(
            model=MODEL_NAME,
            messages=message,
        )


class OpenAIChatModel:
    pass
