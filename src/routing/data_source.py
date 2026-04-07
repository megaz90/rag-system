from pathlib import Path

from src.routing.base import BaseRouter


class DocumentRouter(BaseRouter):
    def __init__(self):
        self.base_path = Path("./data/documents")

    def _discover_categories(self):
        """Automatically find categories from folder structure"""
        categories = {}
        for folder in self.base_path.iterdir():
            if folder.is_dir():
                category_name = folder.stem.replace("_docs", "")
                categories[category_name] = {
                    "folder": folder.name,
                    "path": str(folder),
                    "auto_discovered": True,
                }
        return categories

    def route(self, query: str):
        categories = self._discover_categories()
