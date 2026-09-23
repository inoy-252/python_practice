import csv
import json
import re
from datetime import datetime

import requests


def fetch_market_data(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data["products"]
        else:
            print(f"Server Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Network connection failed: {e}")
        return None


def extract_market_keywords(products):
    descriptions = [p["description"] for p in products]
    combined_text = " ".join(descriptions)
    words = re.findall(r"[a-zA-Z]+", combined_text.lower())
    meaningful_words = [w for w in words if len(w) > 4]
    counts = {}
    for w in meaningful_words:
        counts[w] = counts.get(w, 0) + 1
    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return ranked[:5]


def analyze_market_metrics(products):
    prices = [p["price"] for p in products]
    max_price = max(prices)
    min_price = min(prices)
    avg_price = sum(prices) / len(prices)
    top_product = max(products, key=lambda p: p["price"])
    return {
        "total_products": len(products),
        "max_price": max_price,
        "min_price": min_price,
        "avg_price": round(avg_price, 2),
        "flagship_product": top_product["title"],
    }


def export_market_intelligence(products, metrics, keywords):
    with open("projects/market_pipeline/data/products.json", "w") as f:
        json.dump(products, f, indent=4)
        print("Saved full catalog to data/products.json")

    csv_rows = [
        ["Metric", "Value"],
        ["Total Products", metrics["total_products"]],
        ["Max Price ($)", metrics["max_price"]],
        ["Min Price ($)", metrics["min_price"]],
        ["Average Price ($)", metrics["avg_price"]],
        ["Flagship Product", metrics["flagship_product"]],
        ["Top Keyword", f"{keywords[0][0]} ({keywords[0][1]} mentions)"],
    ]
    with open("projects/market_pipeline/data/summary.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(csv_rows)
        print(" Saved summary spreadsheet to data/summary.csv")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("projects/market_pipeline/logs/pipeline.log", "a") as f:
        f.write(
            f"[{timestamp}] SUCCESS: Ingested {metrics['total_products']} products | Top: {metrics['flagship_product']}\n"
        )
        print(" Execution logged to logs/pipeline.log")


# ==========================================
# PIPELINE EXECUTION ENGINE
# ==========================================
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("MARKET INTELLIGENCE & DATA INGESTION PIPELINE")
    print("=" * 60)

    URL = "https://dummyjson.com/products"

    # Stage 1: Ingestion
    print("\n[STAGE 1/4] Ingesting remote records...")
    products = fetch_market_data(URL)

    if products is not None:
        print(f"[STATUS] Ingestion successful. Total records: {len(products)}")

        # Stage 2: NLP Keyword Analysis
        print("\n[STAGE 2/4] Running NLP keyword extraction...")
        keywords = extract_market_keywords(products)
        print("--- Top Trending Keywords ---")
        for word, count in keywords:
            print(f"  {word:<15} : {count} occurrences")

        # Stage 3: Financial Analytics
        print("\n[STAGE 3/4] Computing market financial metrics...")
        metrics = analyze_market_metrics(products)
        print("--- Executive Metrics Summary ---")
        print(f"  Catalog Size       : {metrics['total_products']} items")
        print(f"  Minimum Price      : ${metrics['min_price']}")
        print(f"  Maximum Price      : ${metrics['max_price']}")
        print(f"  Average Price      : ${metrics['avg_price']}")
        print(f"  Flagship Product   : {metrics['flagship_product']}")

        # Stage 4: File Persistence & Audit Logging
        print("\n[STAGE 4/4] Persisting data structures and audit logging...")
        export_market_intelligence(products, metrics, keywords)

        print("\n" + "=" * 60)
        print("[SUCCESS] Pipeline completed with exit code 0.")
        print("=" * 60 + "\n")

    else:
        print("\n[ERROR] Pipeline terminated: Unable to fetch source data.\n")
