def recall_at_k(ranked: list[str], relevant: set[str], k: int) -> float:
    if not relevant:
        raise ValueError("Relevant set cannot be empty.")
    if k <= 0:
        return 0.0

    values: list[str] = ranked[:k]
    intersection_values = set(values) & relevant
    return len(intersection_values) / len(relevant)
