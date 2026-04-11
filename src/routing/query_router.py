from src.core.database import VectorDatabase
from src.core.llm.factory import llm_provider
from src.routing.base import BaseRouter
from src.routing.data_source import DocumentRouter
from src.schemas.query_context import QueryContext


class QueryRouter(BaseRouter):
    def llm_classify(self, context: QueryContext):
        results = VectorDatabase().search_database(context=context, top_result=3)
        retrieved_docs = [doc["text"] for doc in results if results]

        prompt = f"""You are an intelligent routing system.

        You are given:
        - A user query
        - Retrieved documents from an internal database

        Your job is to decide the best way to answer the query.

        Routes:
        1. "llm" → answer directly without retrieval
        2. "rag" → use retrieved documents to answer
        3. "web" → internal data is insufficient or irrelevant

        Rules:
        - If retrieved documents strongly match the query → choose "rag"
        - If documents are weak, irrelevant, or low confidence → choose "web"
        - If query is conceptual or does not require factual grounding → choose "llm"

        Consider:
        - relevance of documents
        - coverage of information
        - completeness of context

        Return JSON ONLY:
        {
        "route": "...",
        "confidence": 0.0-1.0,
        "doc_relevance_assessment": "high/medium/low"
        }

        Query:
        {context.query}

        Retrieved Documents:
        {retrieved_docs}
        """

        response = llm_provider().generate(prompt)

        return response.message.content

    def rag_pipeline(self, context: QueryContext):
        DocumentRouter().route(context)

    def llm_pipeline(self):
        pass

    def web_search_pipeline(self):
        pass

    def route(self, context: QueryContext) -> None:
        classification = self.llm_classify(context)
        if classification == "llm":
            self.llm_pipeline()
        elif classification == "rag":
            self.rag_pipeline(context)
        elif classification == "web":
            self.web_search_pipeline()
