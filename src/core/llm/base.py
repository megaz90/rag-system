from abc import ABC, abstractmethod


class BaseLLMChatModel(ABC):
    @abstractmethod
    def generate(self, prompt: str):
        pass
