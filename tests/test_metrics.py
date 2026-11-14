import pytest
from groundtruth.metrics import recall_at_k 


def test_recall_at_k_single_relevant():
    # q001 senaryosu: Tek ilgili etiket 3. sırada
    ranked = ["c1", "c2", "FIBA:41.1", "c4", "c5"]
    relevant = {"FIBA:41.1"}

    assert recall_at_k(ranked, relevant, k=1) == 0.0
    assert recall_at_k(ranked, relevant, k=5) == 1.0


def test_recall_at_k_multiple_distinct_relevant():
    # q002 (iki farklı etiket) senaryosu
    ranked = ["c1", "IFAB:7.1", "FIBA:8.1", "c4", "c5"]
    relevant = {"IFAB:7.1", "FIBA:8.1"}

    assert recall_at_k(ranked, relevant, k=5) == 1.0


def test_recall_at_k_duplicate_predictions():
    # q002 (aynı etiket iki kez döndüğünde set kesişimi tek saymalı)
    ranked = ["c1", "IFAB:7.1", "IFAB:7.1", "c4", "c5"]
    relevant = {"IFAB:7.1", "FIBA:8.1"}

    assert recall_at_k(ranked, relevant, k=5) == 0.5


def test_recall_at_k_empty_relevant_raises_value_error():
    # Boş relevant kümesi verildiğinde ValueError fırlatma kontrolü
    ranked = ["c1", "c2", "c3"]
    relevant = set()

    with pytest.raises(ValueError, match="Relevant set cannot be empty."):
        recall_at_k(ranked, relevant, k=3)
