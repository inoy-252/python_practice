import math
import re
from collections import Counter


def tokenize(text):
    return re.findall(r"[a-zA-Z0-9_\-\/]+", text.lower())


class BM25:
    def __init__(self, documents, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.documents = documents
        self.corpus_size = len(documents)

        self.doc_tokens = []
        self.doc_lens = []

        for doc in documents:
            tokens = tokenize(doc["content"] + " " + doc["title"])
            self.doc_tokens.append(tokens)
            self.doc_lens.append(len(tokens))

        self.avg_doc_len = sum(self.doc_lens) / max(self.corpus_size, 1)

        self.doc_term_freqs = [Counter(tokens) for tokens in self.doc_tokens]

        self.doc_freqs = Counter()
        for tokens in self.doc_tokens:
            unique_terms = set(tokens)
            for term in unique_terms:
                self.doc_freqs[term] += 1

        self.idf = {}
        for term, freq in self.doc_freqs.items():
            self.idf[term] = math.log(
                (self.corpus_size - freq + 0.5) / (freq + 0.5) + 1.0
            )

    def score_document(self, query_tokens, doc_index):
        """
        Calculates the BM25 score for a single document against query tokens.
        """
        score = 0.0
        doc_len = self.doc_lens[doc_index]
        term_freqs = self.doc_term_freqs[doc_index]

        for token in query_tokens:
            if token not in term_freqs:
                continue

            tf = term_freqs[token]
            idf = self.idf.get(token, 0.0)

            # Saturated frequency normalized by document length
            numerator = tf * (self.k1 + 1.0)
            denominator = tf + self.k1 * (
                1.0 - self.b + self.b * (doc_len / self.avg_doc_len)
            )

            score += idf * (numerator / denominator)

        return score

    def search(self, query, top_k=None):
        """
        Ranks all documents in the corpus for the given query.
        Returns a list of dicts with doc, score, and rank.
        """
        query_tokens = tokenize(query)
        if not query_tokens:
            return []

        scored_docs = []
        for i, doc in enumerate(self.documents):
            score = self.score_document(query_tokens, i)
            scored_docs.append({"doc": doc, "score": score})

        # Sort descending by BM25 score
        scored_docs.sort(key=lambda x: x["score"], reverse=True)

        if top_k is not None:
            scored_docs = scored_docs[:top_k]

        # Attach 1-based rank (1st place, 2nd place, etc.)
        for rank, item in enumerate(scored_docs, 1):
            item["rank"] = rank

        return scored_docs

