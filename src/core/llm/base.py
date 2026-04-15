from abc import ABC, abstractmethod


class BaseLLMChatModel(ABC):
    @abstractmethod
    def generate(
        self,
        system_content: str,
        user_content: str,
    ):
        pass
