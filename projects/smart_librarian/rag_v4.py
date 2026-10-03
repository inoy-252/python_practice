"""
Smart Librarian RAG v4: Production Retrieval-Augmented Generation.
Features Dense Semantic Embeddings + NumPy Cosine Similarity + Gemini 3.8 Flash Generation.
"""

import numpy as np
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

page_1 = (
    "PUBG is an action based online game where players try to eliminate each other "
    "using loot supplies like: guns, grenades, cars. This game has also a bluezone, "
    "redzone where players are likely to get eliminated if they don't have the supplies."
)
page_2 = (
    "Chess is a game of tactics and strategies. This is a game played by two players "
    "at a time and the goal is to corner the other player's king and that is called checkmate. "
    "Some famous chess players are: Magnus Carlsen, Gary Kasparov, Hikaru Nakamura."
)
page_3 = (
    "Football is one of the greatest sport to be ever played. A total of 22 players "
    "divided equally into two teams of 11 players play against each other trying to put "
    "the ball into other team's net and that is how you score a goal. The legends of football "
    "are Cristiano Ronaldo, Lionel Messi, Pele, Maradona and some of the greatest teams include: "
    "Manchester United, Real Madrid, Barcelona, Liverpool."
)

documents = [
    {"topic": "PUBG", "content": page_1, "embedding": None},
    {"topic": "Chess", "content": page_2, "embedding": None},
    {"topic": "Football", "content": page_3, "embedding": None},
]


def cosine_similarity(vec_a, vec_b):
    dot_prod = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)

    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0

    return float(dot_prod / (norm_a * norm_b))


def get_embedding(text):
    response = client.models.embed_content(model="gemini-embedding-001", contents=text)
    assert response.embeddings is not None
    return np.array(response.embeddings[0].values)


print("=" * 60)
print("INDEXING: Generating semantic vectors for knowledge documents...")
for doc in documents:
    doc["embedding"] = get_embedding(doc["content"])
    print(
        f"   Indexed: [{doc['topic']}] into {len(doc['embedding'])}-dimensional vector."
    )

print("All documents indexed into vector space!\n" + "=" * 60)


def retrieve_best_doc(query, documents):
    query_vec = get_embedding(query)

    best_doc = None
    best_score = -1.0

    print("\n--- Vector Similarity Breakdown ---")
    for doc in documents:
        score = cosine_similarity(query_vec, doc["embedding"])
        print(f"  Topic: {doc['topic']:<10} | Similarity Score: {score:.4f}")

        if score > best_score:
            best_score = score
            best_doc = doc

    print("----------------------------------")
    return best_doc, best_score


def generate_grounded_answer(query, context):
    prompt = f"""You are Smart Librarian, an expert AI knowledge assistant.
Answer the user's question using the retrieved library context below.
- Synthesize facts and recognize synonyms or related terms (e.g., rifles are guns; shrinking danger zones refer to the bluezone/redzone).
- State the name of the topic/game and explain how the context answers the user's question.
- If the question genuinely cannot be answered from the context even with synonyms, state: "I do not have enough information in my library to answer that."

CONTEXT:
{context}

USER QUESTION:
{query}

GROUNDED ANSWER:"""
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite", contents=prompt
        )
    except Exception:
        response = client.models.generate_content(
            model="gemini-3.8-flash", contents=prompt
        )
    assert response.text is not None
    return response.text.strip()


SIMILARITY_THRESHOLD = 0.50

print("\nSmart Librarian RAG v4 is ready! Ask anything about the library.")
print("Type 'quit' to exit.")

while True:
    user_query = input("\n Ask a question: ").strip()
    if user_query.lower() == "quit":
        print("\nThank you for using Smart Librarian RAG v4. Goodbye!")
        break

    if not user_query:
        continue

    best_doc, best_score = retrieve_best_doc(user_query, documents)

    if best_score < SIMILARITY_THRESHOLD or best_doc is None:
        print("\nFALLBACK TRIGGERED:")
        print("   No sufficiently relevant knowledge found in the library.")
        print(
            f"   (Highest similarity was {best_score:.4f}, below required threshold {SIMILARITY_THRESHOLD:.2f})"
        )
        continue
    print(f"\nRETRIEVED TOPIC: [{best_doc['topic']}] (Confidence: {best_score:.4f})")
    print(" Synthesizing grounded answer with Gemini 3.5 Flash Lite...")
    final_answer = generate_grounded_answer(user_query, best_doc["content"])

    print("\n" + "=" * 60)
    print("SMART LIBRARIAN ANSWER:")
    print(final_answer)
    print("=" * 60)
    print(f"Source Citation: Smart Librarian Knowledge Base -> [{best_doc['topic']}]")
