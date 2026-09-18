page_1 = "PUBG is an action based game where players try to eliminate each other using loot supplies like: guns, grenads, cars. This game has also a bluezone, redzone where players are likely to get eliminated if they don't have the supplies"
page_2 = "Chess is a game of tactics and strategies. This is a game played by two players at a time and the goal is to corner the other player's king and that is called checkmate. Some famous chess players are: Magnus Carlsen, Gary Kasparov, Hikaru Nakamura"
page_3 = "Football is one of the greatest sport to be ever played. A total of 22 players divided equally into two teams of 11 players play agianst each other trying to put the ball into other team's net and that is how you score a goal.The legends of football are Cristiano Ronaldo, Lionel Messi, Pele, Maradona and some of the greatest teams include: Manchester United, Real Madrid, Barcelona, Liverpool. "
document = [page_1, page_2, page_3]
clean_page1 = page_1.replace(",", "")
page_1_words = set(clean_page1.lower().split())
clean_page2 = page_2.replace(",", "")
page_2_words = set(clean_page2.lower().split())
clean_page3 = page_3.replace(",", "")
page_3_words = set(clean_page3.lower().split())
question = input("Ask the Smart Librarian a question: ")
clean_question = question.replace("?", "")
question_words = set(clean_question.lower().split())
comparison_1 = question_words.intersection(page_1_words)
comparison_2 = question_words.intersection(page_2_words)
comparison_3 = question_words.intersection(page_3_words)
print(f"Your question had {len(comparison_1)} words {comparison_1} matching topic PUBG")
print(
    f"Your question has {len(comparison_2)} words {comparison_2} matching the topic chess"
)
print(
    f"Your question had {len(comparison_3)} words {comparison_3} matching the topic football"
)
print("=" * 50)
print(" SMART LIBRARIAN: INOY")
print("=" * 50)
print(f"\n[USER PROMPT]:\n{question}")
print(
    "[AI DIRECTIVE]:\nConsult the page with the highest matching words to provide a factual answer."
)
if len(comparison_1) > len(comparison_2) and len(comparison_1) > len(comparison_3):
    print(
        f"Your question is about PUBG so here is  information regarding the same\n {page_1}"
    )
elif len(comparison_2) > len(comparison_1) and len(comparison_2) > len(comparison_3):
    print(
        f"Your question is about Chess so here is information regarding the same\n {page_2}"
    )
elif len(comparison_3) > len(comparison_1) and len(comparison_3) > len(comparison_2):
    print(f"Your question is about Football...\n{page_3}")
else:
    print(
        "Sorry! The Smart Librarian could not find any relevant information on this topic."
    )
print("=" * 50)
