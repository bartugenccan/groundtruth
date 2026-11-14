import json, re, urllib.request
import numpy as np
from rank_bm25 import BM25Okapi

DOCS = {
    "D1": "If the connection is refused, check that the server is running. Error code: ECONNREFUSED.",
    "D2": "Cannot reach the server? Review your firewall and network settings.",
    "D3": "Card details are encrypted on the payment page.",
}
QUERIES = {
    "Q1": "what does ECONNREFUSED mean",
    "Q2": "my app can't connect to the backend",
}


def tokenize(text):
    return re.findall(r"[a-z0-9_']+", text.lower())


def embed(texts):
    req = urllib.request.Request(
        "http://localhost:11434/api/embed",
        data=json.dumps({"model": "nomic-embed-text", "input": texts}).encode(),
        headers={"Content-Type": "application/json"},
    )
    return np.array(json.load(urllib.request.urlopen(req))["embeddings"])


def cosine(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


ids = list(DOCS)
bm25 = BM25Okapi([tokenize(DOCS[i]) for i in ids])
doc_vecs = embed([DOCS[i] for i in ids])

for qid, q in QUERIES.items():
    print(f"\n{qid}: {q!r}   tokens={tokenize(q)}")
    bm = bm25.get_scores(tokenize(q))
    qv = embed([q])[0]
    print(f"  {'doc':<4} {'bm25':>8} {'cosine':>8}")
    for i, d in enumerate(ids):
        print(f"  {d:<4} {bm[i]:>8.3f} {cosine(qv, doc_vecs[i]):>8.3f}")
