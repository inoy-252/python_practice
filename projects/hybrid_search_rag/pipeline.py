from bm25 import BM25
from data import DOCUMENTS
from dense_retriever import DenseRetriever
from fusion import reciprocal_rank_fusion
from reranker import Reranker

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
