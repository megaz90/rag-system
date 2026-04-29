import json
from typing import Dict

from src.core.database import VectorDatabase
from src.core.llm.factory import llm_provider
from src.generation.generator import LLMResponseGenerator
from src.routing.base import BaseRouter
from src.routing.data_source import DocumentRouter
from src.schemas.query_context import QueryContext


class QueryRouter(BaseRouter):
    def _execute(self, route: str, context: QueryContext) -> None:
        if route == "llm":
            self.llm_pipeline(context)
        elif route == "rag":
            self.rag_pipeline(context)
        elif route == "web":
            self.web_search_pipeline(context)

    def _fallback(self, route, context):
        # If LLM route fails, try a different route
        # This means we already tried llm but confidence was too low so we try a different route
        if route == "llm":
            self.rag_pipeline(context)

        # If RAG route fails, try a different route likely a web search
        if route == "rag":
            self.web_search_pipeline(context)

        if route == "web":
            self.llm_pipeline(context)

        self.llm_pipeline(context)

    def llm_classify(self, context: QueryContext) -> Dict:
        results = VectorDatabase().search_database(context=context, top_result=3)
        retrieved_docs = [doc["text"] for doc in results if results]

        system_prompt = """You are an intelligent query routing system.

        Your task: Analyze the user's query and retrieved documents, then decide the best route.

        AVAILABLE ROUTES:
        1. "rag" → Use retrieved documents (they contain the answer)
        2. "web" → Search the web (documents are insufficient/irrelevant)
        3. "llm" → Answer from general knowledge (no external data needed)

        ROUTING LOGIC:

        Choose "rag" when:
        - Documents directly answer the query
        - Information is specific to the internal system/company
        - At least 1 document is highly relevant

        Choose "web" when:
        - Documents are off-topic or weakly related
        - Query asks about recent events, external info, or current data
        - Documents provide partial info but are incomplete

        Choose "llm" when:
        - Query is general knowledge (definitions, concepts, how-to)
        - No specific facts or data are required
        - Query is conversational or opinion-based

        CONFIDENCE SCALE:
        - 0.9-1.0 = very certain about route
        - 0.7-0.89 = confident but could use alternative
        - 0.5-0.69 = uncertain, borderline decision
        - below 0.5 = low confidence, might be wrong route

        OUTPUT FORMAT (strict JSON):
        {
        "route": "rag" | "web" | "llm",
        "confidence": 0.85,
        }
        """

        user_prompt = f"""Query:
        {context.query}

        Retrieved Documents:
        {retrieved_docs}

        Determine the best route:"""

        response = llm_provider().generate(
            user_content=user_prompt, system_content=system_prompt
        )

        return json.loads(response.message.content)

    def rag_pipeline(self, context: QueryContext) -> str:
        return DocumentRouter().route(context)

    def llm_pipeline(self, context: QueryContext):
        system_prompt = """You are a highly reliable AI assistant operating in LLM-only mode.

        You do not have access to external databases, documents, or the internet.

        Your job is to answer using general knowledge and reasoning only.

        RULES:
        - Do not fabricate facts, numbers, citations, or sources.
        - If the question requires external, private, or real-time information, clearly say you do not have access to it.
        - If uncertain, explicitly state the uncertainty instead of guessing.
        - Prefer correctness over completeness.
        - Be clear, structured, and direct.
        - Avoid unnecessary explanation unless the user asks for it.
        """

        user_prompt = f"""Answer the following question using general knowledge only.

        Question:
        {context.query}

        Requirements:
        - Be accurate
        - Do not assume unknown facts
        - If information is uncertain, say so
        - Keep the answer clear and useful
        """

        response = LLMResponseGenerator().generate_answer(
            user_prompt=user_prompt, system_prompt=system_prompt
        )
        return response.message.content

    def web_search_pipeline(self, context: QueryContext):
        """
        For now the web search leads to llm pipeline to answer.
        TODO: Implement web search pipeline and remove this method
        """
        self.llm_pipeline(QueryContext(query="What is the capital of France?"))

    def route(self, context: QueryContext) -> None:
        classification = self.llm_classify(context)

        route = classification["route"]
        confidence = classification["confidence"]

        # High confidence → trust
        if confidence >= 0.75:
            print(self._execute(route, context))

        # Medium confidence try + fallback
        if 0.6 <= confidence < 0.75:
            print(self._execute(route, context))

        print(self._fallback(route, context))
