from src.core.database import VectorDatabase
from src.core.llm.factory import llm_provider
from src.generation.generator import LLMResponseGenerator
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

        print(response.message.content)

    def web_search_pipeline(self):
        pass

    def route(self, context: QueryContext) -> None:
        classification = self.llm_classify(context)
        if classification == "llm":
            self.llm_pipeline(context)
        elif classification == "rag":
            self.rag_pipeline(context)
        elif classification == "web":
            self.web_search_pipeline()
