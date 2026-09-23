# 🌐 Autonomous Market Intelligence Pipeline

A resilient, production-grade **ETL (Extract, Transform, Load)** pipeline built in pure Python. It ingests live product data from remote web APIs, cleans unstructured marketing text using NLP & Regular Expressions, computes financial analytics, and persists data across structured formats (`.json`, `.csv`, `.log`).

---

## 🏗️ System Architecture

```text
       [ Live Web API ]
              │ (requests.get with 5s timeout)
              ▼
   ┌───────────────────────┐
   │ Stage 1: Ingestion    │ ───> [ Network Failure? ] ──> Graceful Exit (None)
   │ (try/except shield)   │
   └───────────────────────┘
              │ (30 Product Records)
              ▼
   ┌───────────────────────┐
   │ Stage 2: NLP Cleaning │ ───> Combines text with .join()
   │ (RegEx tokenization)  │ ───> Filters noise (len > 4)
   │                       │ ───> Ranks top keywords with lambda
   └───────────────────────┘
              │
              ▼
   ┌───────────────────────┐
   │ Stage 3: Analytics    │ ───> Min, Max, Average prices
   │ (List Comprehension)  │ ───> Identifies Flagship Product
   └───────────────────────┘
              │
              ▼
   ┌───────────────────────────────────────────────────────────┐
   │ Stage 4: File Persistence & Audit Logging                 │
   │  ├── data/products.json  (Full catalog with indent=4)     │
   │  ├── data/summary.csv   (Executive 2-column spreadsheet)  │
   │  └── logs/pipeline.log  (Timestamped execution history)   │
   └───────────────────────────────────────────────────────────┘
```

---

## 🧠 The 4 Core Stages Explained Simply

### 1. Stage 1: The Resilient Fetcher (`fetch_market_data`)
* **The Problem:** The internet is unpredictable. A server might crash (`500`), a page might be missing (`404`), or your Wi-Fi might drop.
* **The Solution:** We wrap the request in a `try / except` shield:
  - **`try:`** Attempts to download the data with `requests.get(url, timeout=5)`.
  - **`if status_code == 200:`** If the server gave the green light, we parse with `.json()` and return the products.
  - **`else:`** If the server returned an error (like 404), we print the error and return `None`.
  - **`except Exception as e:`** If the Wi-Fi completely failed, it catches the crash and returns `None`.
* **Key Lesson:** The pipeline *never* crashes; it reports errors gracefully.

---

### 2. Stage 2: NLP Keyword Extraction (`extract_market_keywords`)
* **The Problem:** Each product has a description full of messy punctuation (`!`, `,`), mixed casing (`"Mascara"` vs `"mascara"`), and filler words (`"and"`, `"the"`).
* **The Solution:**
  1. `[p["description"] for p in products]`: Pulls all 30 descriptions into a list.
  2. `" ".join(...)`: Glues all 30 descriptions into one continuous paragraph.
  3. `re.findall(r"[a-zA-Z]+", combined_text.lower())`: Extracts only pure lowercase English words.
  4. `[w for w in words if len(w) > 4]`: Discards short filler words, keeping only meaningful words.
  5. `counts[w] = counts.get(w, 0) + 1`: Keeps an automatic tally score for each word.
  6. `sorted(counts.items(), key=lambda item: item[1], reverse=True)[:5]`: Sorts by count (highest first) and returns the top 5 winners!

---

### 3. Stage 3: Financial Analytics (`analyze_market_metrics`)
* **The Problem:** Business leaders need executive summaries, not 30 raw product objects.
* **The Solution:**
  - `prices = [p["price"] for p in products]`: Extracts a clean list of numbers.
  - `max(prices)` & `min(prices)`: Finds price extremes.
  - `sum(prices) / len(prices)`: Computes the average price.
  - `max(products, key=lambda p: p["price"])`: Finds the single product dictionary with the highest price tag.
  - Returns a clean summary dictionary.

---

### 4. Stage 4: Dual Storage & Audit Logging (`export_market_intelligence`)
* **Task A (JSON Storage):** `json.dump(products, f, indent=4)` saves the full structured records to `data/products.json`.
* **Task B (CSV Storage):** `csv.writer(f).writerows(csv_rows)` creates a neat 2-column spreadsheet in `data/summary.csv`.
* **Task C (Audit Logging):** `open("logs/pipeline.log", "a")` opens the log file in **Append mode**. It grabs the exact second with `datetime.now().strftime(...)` and writes a permanent paper trail of the run without deleting past history.

---

## 📁 Data Artifacts & Output Schema

The pipeline automatically writes to the following structured endpoints:

| Artifact | Format | Description |
| :--- | :--- | :--- |
| **`data/products.json`** | JSON | Full raw catalog with formatted indentation (`indent=4`) for downstream model ingestion. |
| **`data/summary.csv`** | CSV | Tabular executive KPI summary formatted for spreadsheet analysis. |
| **`logs/pipeline.log`** | Plain Text | Persistent, timestamped append-only audit trail logging every pipeline execution. |

---

## 🚀 How to Run

From the root of `30-days-of-python-practice`:

```bash
python3 projects/market_pipeline/app.py
```
