from bm25 import BM25
from data import DOCUMENTS
from dense_retriever import DenseRetriever
from dotenv import load_dotenv
from fusion import reciprocal_rank_fusion
from google import genai
from reranker import Reranker

load_dotenv()
client = genai.Client()


def generate_answer(query, document):
    prompt = f"""You are a helpful engineering assistant. 
Answer the engineer's question using ONLY the information in the document below.
If the document does not contain the answer, say "This document does not cover that."

Engineer's Question: {query}

Document Title: {document["title"]}
Document Content:
{document["content"]}

Provide a clear, direct, actionable answer."""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )
    return response.text.strip() if response.text else "No answer generated."


print("Initializing Hybrid Search RAG Pipeline...")
print("Loading BM25 index...")
bm25 = BM25(DOCUMENTS)

print("Generating document embeddings (this may take a few seconds)...")
dense = DenseRetriever(DOCUMENTS)

print("Loading reranker...")
reranker = Reranker()

print("\nPipeline ready.")
print("=" * 55)

while True:
    query = input("\nEnter your query (or 'quit' to exit): ").strip()

    if not query:
        continue
    if query.lower() == "quit":
        print("Exiting pipeline.")
        break
    print(f"\nSearching for: '{query}'")
    print("-" * 55)

    bm25_results = bm25.search(query, top_k=5)
    dense_results = dense.search(query, top_k=5)

    fused = reciprocal_rank_fusion(bm25_results, dense_results)
    top_candidates = [doc for doc, _ in fused[:3]]

    print("Reranking top candidates...")
    final_results = reranker.rerank(query, top_candidates)

    print("\n=== FINAL RESULTS ===")
    for rank, (doc, score) in enumerate(final_results, start=1):
        print(f"\nRank #{rank} | Relevance: {score:.1f}/10.0")
        print(f"ID   : {doc['id']}")
        print(f"Title: {doc['title']}")

    best_doc = final_results[0][0]
    print("\n=== GENERATED ANSWER ===")
    print(generate_answer(query, best_doc))
