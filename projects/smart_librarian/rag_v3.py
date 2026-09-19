page_1 = "PUBG is an action based game where players try to eliminate each other using loot supplies like: guns, grenads, cars. This game has also a bluezone, redzone where players are likely to get eliminated if they don't have the supplies"
page_2 = "Chess is a game of tactics and strategies. This is a game played by two players at a time and the goal is to corner the other player's king and that is called checkmate. Some famous chess players are: Magnus Carlsen, Gary Kasparov, Hikaru Nakamura"
page_3 = "Football is one of the greatest sport to be ever played. A total of 22 players divided equally into two teams of 11 players play agianst each other trying to put the ball into other team's net and that is how you score a goal.The legends of football are Cristiano Ronaldo, Lionel Messi, Pele, Maradona and some of the greatest teams include: Manchester United, Real Madrid, Barcelona, Liverpool. "
documents = [
    {"topic": "PUBG", "content": page_1},
    {"topic": "Chess", "content": page_2},
    {"topic": "Football", "content": page_3},
]


def clean_and_tokenize(text):
    clean_text = (
        text.replace(".", "").replace("?", "").replace(",", "").replace(":", "")
    )
    words = set(clean_text.lower().split())
    stop_words = {
        "is",
        "an",
        "and",
        "a",
        "the",
        "to",
        "of",
        "in",
        "it",
        "are",
        "they",
        "this",
        "that",
        "who",
        "how",
        "what",
        "where",
        "when",
        "why",
    }
    return words - stop_words


def retrieve_best_document(query, documents):
    query_words = clean_and_tokenize(query)
    best_score = 0
    best_doc = None
    for doc in documents:
        doc_words = clean_and_tokenize(doc["content"])
        mathcing_words = query_words.intersection(doc_words)
        score = len(mathcing_words)
        if score > best_score:
            best_score = score
            best_doc = doc
    return best_score, best_doc


while True:
    query = input("\nAsk the Smart Librarian a question (or type 'quit' to exit): ")
    if query.lower() == "quit":
        print("\nGoodbye! Have a great day.")
        break
    best_score, best_doc = retrieve_best_document(query, documents)
    if best_doc is not None:
        print("=" * 50)
        print(f" MATCH FOUND! Topic: {best_doc['topic']} (Score: {best_score})")
        print("=" * 50)
        print(f"[RETRIEVED KNOWLEDGE]:\n{best_doc['content']}")
        print("=" * 50)
    else:
        print("=" * 50)
        print("Sorry! No relevant information was found in the database.")
        print("=" * 50)
