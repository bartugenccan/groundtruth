import math


def recall_at_k(ranked: list[str], relevant: set[str], k: int) -> float:
    if not relevant:
        raise ValueError("Relevant set cannot be empty.")
    if k <= 0:
        raise ValueError("k cannot be zero or below zero")

    values: list[str] = ranked[:k]
    intersection_values = set(values) & relevant
    return len(intersection_values) / len(relevant)


def reciprocal_rank(ranked: list[str], relevant: set[str], k: int) -> float:
    if not relevant:
        raise ValueError("Relevant set cannot be empty.")
    if k <= 0:
        raise ValueError("k cannot be zero or below zero")

    for i, doc_id in enumerate(ranked[:k], start=1):
        if doc_id in relevant:
            return 1 / i

    return 0.0


def ndcg_at_k(ranked: list[str], relevant: set[str], k: int) -> float:
    if not relevant:
        raise ValueError("Relevant set cannot be empty.")
    if k <= 0:
        raise ValueError("k cannot be zero or below zero")

    dcg = 0

    for i, doc_id in enumerate(ranked[:k], start=1):
        if doc_id in relevant:
            dcg += 1 / math.log2(i + 1)

    ideal_accuracy = min(len(relevant), k)
    idcg = 0

    for i in range(1, ideal_accuracy + 1):
        idcg += 1 / math.log2(i + 1)

    return dcg / idcg
