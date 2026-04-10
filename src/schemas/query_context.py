from dataclasses import dataclass
from typing import List, Optional


@dataclass
class QueryContext:
    query: str
    sources: Optional[List[str]] = None
    rewritten_query: str | None = None
