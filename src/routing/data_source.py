import json
from pathlib import Path
from typing import Dict, List, Tuple

from src.core.llm.factory import llm_provider
from src.retrieval.query import RAGQuerier
from src.routing.base import BaseRouter
from src.schemas.query_context import QueryContext


class DocumentRouter(BaseRouter):
    """
    Routes user queries to the most relevant document categories using an LLM-based classifier with fallback heuristics.
    """

    def __init__(self):
        self.base_path = Path("./data/documents")

    def _discover_categories(self) -> Dict:
        """
        Dynamically discovers available document categories based on folder structure under the base path.

        Each folder represents a category.
        """
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

    def _parse_and_validate(self, response: str) -> Tuple[List[str], float]:
        """
        Parses LLM response and validates output format.

        Ensures:
        - Response is valid JSON
        - Only allowed sources are returned
        - Confidence is extracted safely

        Args:
            response (str): Raw LLM response content

        Returns:
            Tuple[List[str], float]: (validated_sources, confidence_score)
        """
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

    def fetch_data_source(self, context: QueryContext) -> List[str]:
        """
        Uses an LLM-based router to select the most relevant document categories for a given user query.

        Includes:
        - Dynamic category discovery
        - LLM-based classification
        - JSON structured output parsing
        - Confidence-based fallback strategy

        Args:
            context (QueryContext)

        Returns:
            List[str]: Selected document categories (max top 2)
        """
        all_sources_keys = list(self._discover_categories().keys())

        sources_str = "\n".join(all_sources_keys)

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
            "confidence": 0.0
            }}
            """
        response = llm_provider(system_content=system_prompt).generate(context.query)

        filtered_sources, confidence = self._parse_and_validate(
            response.message.content
        )

        # If confidence is less than 0.5, return all sources
        if confidence < 0.5:
            return all_sources_keys

        # Returning top 2 sources
        return filtered_sources[:2] if len(filtered_sources) > 2 else filtered_sources

    def route(self, context: QueryContext) -> None:
        """
        Entry point for routing a query into the RAG pipeline.

        Steps:
        1. Determine relevant document categories
        2. Build filtered QueryContext
        3. Pass to RAGQuerier for answer generation

        Args:
            context (QueryContext)
        """
        data_sources = self.fetch_data_source(context)

        RAGQuerier().ask_question(
            QueryContext(query=context.query, sources=data_sources)
        )
