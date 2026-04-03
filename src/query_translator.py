from typing import Dict, List

from src.core.database import db
from src.core.llm.factory import llm_provider


class QueryTranslator:
    """
    Handles different query translation strategies for improving retrieval in RAG systems.

    This class expands or transforms a user query into multiple alternative forms to improve retrieval coverage from a
    vector database. Different translation strategies help overcome limitations of single-query semantic search.

    Supported Query Translation Strategies:

    1. Multi-Query Generation
    2. Multi-Query Generation using Reciprocal Rank Fusion (RRF)
    3. Step-back / Abstraction Query
    4. Decomposition (Sub-question Generation)
    5. Hypothetical Document Embeddings (HyDE)

    Each strategy improves retrieval quality by increasing diversity and coverage
    of search space before applying ranking or fusion techniques (e.g., RRF).
    """

    def fetch_relevant_docs(self, prompt: str) -> List[List[Dict]]:
        """
        Fetch relevant documents from the vector database based on the prompt.
        """
        response = llm_provider().generate(prompt)

        queries = str(response.message.content).split("\n")

        docs = []
        for query in queries if queries else []:
            results = db.search_database(query)
            if not results:
                print("No results returned from DB.")
                continue

            docs.append(results)

        return docs

    def multi_query_translator(self, question: str) -> List[Dict]:
        """
        Multi query translator method takes a question from the user and returns a list of alternative questions.
        This is a "Sub-question" strategy which breaks down the user query into multiple questions.
        It goes through following steps:

        1. Generate a prompt for the LLM
        2. Send the prompt to the LLM along with the user query
        3. Return the response from the LLM
        4. Process the response and return a list of alternative questions
        5. Search the vector database using the alternative questions
        6. Returns the unique results so that there are not duplicates
        """
        prompt = f"""You are an AI language model assistant. your task is to generate five different versions of the 
        given user question to retrieve the relevant information from the documents from a vector database. By 
        generating multiple perspectives on the user question, your goal is to help the user overcome some of the 
        limitations of the distance-based similarity search.
        Provide these alternative questions separated by newlines. Original question: {question}"""

        docs = self.fetch_relevant_docs(prompt)

        seen = set()
        unique_docs = []

        for doc_list in docs:
            for doc in doc_list:
                key = doc.get("id")
                if key not in seen:
                    seen.add(key)
                    unique_docs.append(doc)

        return unique_docs

    def reciprocal_rank_fusion(self, results: List[List], k: int = 60) -> List[Dict]:
        """
        Combines multiple ranked retrieval result lists using Reciprocal Rank Fusion (RRF).
        This method merges document rankings from multiple query results into a single unified ranking.
        Each document's final score is computed using the RRF formula:
            score(doc) += 1 / (rank + k)

        where:
            - `rank` is the position of the document in each individual result list (1-based)
            - `k` is a smoothing constant that reduces the impact of high-ranked positions (Usually k = 60)

        The method aggregates scores across all input lists, sorts documents by their fused score in descending order,
        and returns the final ranked list of documents.
        """
        fusion_score = {}
        for doc_list in results:
            for rank, doc in enumerate(doc_list, start=1):
                key = doc.get("id")

                if key not in fusion_score:
                    fusion_score[key] = {"score": 0, "doc": doc}

                # Update the score using the RRF formula
                fusion_score[key]["score"] += 1 / (rank + k)

        # We are just sorting the dictionary here based on the fusion score not the key
        # Example: fusion_score = {"doc1": {"score": 0.032, "doc": doc1}, "doc2": {"score": 0.045, "doc": doc2}}
        sorted_docs = sorted(
            fusion_score.values(), key=lambda x: x["score"], reverse=True
        )

        return [item["doc"] for item in sorted_docs]

    def rag_fusion_translator(self, question: str) -> List[Dict]:
        """
        Performs multi-query RAG fusion retrieval using Reciprocal Rank Fusion (RRF).

        This method implements a RAG-Fusion strategy where a single user question is expanded into multiple alternative
        search queries using an LLM. Each query is independently used to retrieve relevant documents.

        The retrieved results from all queries are then combined using Reciprocal Rank Fusion (RRF), which re-ranks
        documents based on their relative positions across multiple ranked lists rather than raw similarity scores.
        """

        prompt = f"""You are a helpful assistant that generates multiple search queries based on a single input query.\n
        Generate multiple search queries related to: {question} \n
        Output (4 queries):"""

        docs = self.fetch_relevant_docs(prompt)

        return self.reciprocal_rank_fusion(docs)

    def step_back_translator(self, question: str):
        """
        TODO: Implementation to be added.
        """
        pass
    
    def decomposition_translator(self, question: str):
        """
        TODO: Implementation to be added.
        """
        pass
    
    def hyde_translator(self, question: str):
        """
        TODO: Implementation to be added.
        """
        pass