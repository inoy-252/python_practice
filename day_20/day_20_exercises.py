import re

import requests

url = "https://dummyjson.com/products"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    products = data["products"]

    print(f"Total products fethced: {len(products)}")
    prices = [p["price"] for p in products]

    print("\n--- All 30 Products ---")
    for p in products:
        print(f"- {p['title']}: ${p['price']}")

    max_price = max(prices)
    min_price = min(prices)
    avg_price = sum(prices) / (len(prices))

    print(f"Most expensive: {max_price}")
    print(f"Cheapest: {min_price}")
    print(f"Average price: {avg_price:.2f}")

    top_product = max(products, key=lambda p: p["price"])
    print(f"Top product: {top_product['title']}  priced at {top_product['price']} $ ")

else:
    print(f"Request failed with status: {response.status_code}")


raw_text = """
AI and Machine Learning are transforming modern technology! 
With Python, AI engineers can train deep neural networks. 
Python makes AI accessible, powerful, and fast. #AI #Python @TechToday
"""

print("=" * 50)
words = re.findall(r"[a-zA-Z]+", raw_text.lower())
print(f"clean words extracted: {len(words)}")

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
ranked_words = sorted(counts.items(), key=lambda item: item[1], reverse=True)


print("\n Top 3 Keywords in Text:")
for word, count in ranked_words[:3]:
    print(f"  • '{word}': appears {count} times")
