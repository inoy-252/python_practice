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
