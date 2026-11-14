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

    for i, doc_id in enumerate(ranked[:k], start = 1):
        if doc_id in relevant:
            return 1/i

    return 0.0
    


        
