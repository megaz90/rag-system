from typing import TypedDict


class Document(TypedDict):
    name: str
    path: str
    text: str
    category: str
    type: str
