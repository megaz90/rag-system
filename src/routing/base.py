from abc import ABC, abstractmethod


class BaseRouter(ABC):
    @abstractmethod
    def route(self, query: str):
        pass
