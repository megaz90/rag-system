from abc import ABC, abstractmethod

from src.schemas.query_context import QueryContext


class BaseRouter(ABC):
    @abstractmethod
    def route(self, context: QueryContext):
        pass
