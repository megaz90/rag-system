import json
from pathlib import Path
from typing import Dict

from src.core.llm.factory import llm_provider
from src.routing.base import BaseRouter


class DocumentRouter(BaseRouter):
    def __init__(self):
        self.base_path = Path("./data/documents")

    def _discover_categories(self) -> Dict:
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

    def _parse_and_validate(self, response):
        try:
            data = json.loads(response)
            sources = [
                s
                for s in data.get("sources", [])
                if s in self._discover_categories().keys()
            ]
            confidence = data.get("confidence", 0.0)
            return sources, confidence
        except Exception as e:
            print(e)
            return [], 0.0

    def _fetch_data_source(self, query: str):
        sources_str = "\n".join(self._discover_categories().keys())
        system_prompt = f"""You are a data source router.
            Available sources:
            {sources_str}

            Select the MOST relevant sources for the query and overall confidence level of the selection.

            Rules:
            - Only choose from the given sources
            - Return ONLY valid JSON
            - Do not explain

            Confidence definition:
            - 1.0 = extremely certain
            - 0.7 = likely correct
            - 0.5 = uncertain but reasonable
            - below 0.5 = weak match
            
            Format:
            {{
            "sources": ["source_name", ....]
            "confidence": 0.0 - 1.0
            }}
            """
        response = llm_provider(system_content=system_prompt).generate(query)

        sources, confidence = self._parse_and_validate(response.message.content)

        return sources

    def route(self, query: str):
        self._fetch_data_source(query)
