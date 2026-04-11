from typing import Dict, List

from ollama import ChatResponse, chat

from src.core.config import MODEL_NAME
from src.core.llm.base import BaseLLMChatModel
from src.prompts.system_prompts import DEFAULT_SYSTEM_PROMPT


class OllamaChatModel(BaseLLMChatModel):
    """
    Wrapper for ollama chat model
    """

    def __init__(self):
        self.system_content = DEFAULT_SYSTEM_PROMPT

    def build_messages(self, system_content: str, user_content: str) -> List[Dict]:
        return [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
        ]

    def generate(
        self,
        user_content: str,
        system_content: str | None = None,
    ) -> ChatResponse:
        """
        TODO: Add a normalizer function to normalize the response
        """
        if system_content is None:
            system_content = self.system_content

        messages = self.build_messages(
            system_content=system_content, user_content=user_content
        )
        try:
            return chat(
                model=MODEL_NAME,
                messages=messages,
            )

        except Exception as e:
            raise RuntimeError(f"LLM generation failed: {e}")


class OpenAIChatModel(BaseLLMChatModel):
    """
    TODO: Add OpenAIChatModel
    """

    def generate(self, prompt: str):
        pass
