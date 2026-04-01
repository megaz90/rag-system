from core.database import db


def search_database(query: str, top_result: int = 3):
    """
    Search for documents similar to the query.

    query: the user's question
    top_result: how many results to return
    """
    query_embeddings = db.embedding_model.encode([query])[0].tolist()
    collection = db.chroma_client.create_collection(name="test")

    results = collection.query(query_embeddings=query_embeddings, n_results=top_result)

    return results["documents"][0] if results["documents"] else results["documents"]
