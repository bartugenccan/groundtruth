import pytest
from groundtruth.metrics import recall_at_k, reciprocal_rank


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

def test_reciprocal_rank():
    # 1. q001 (3. sırada isabet)
    q001_ranked = ["c1", "c2", "FIBA:41.1", "c4", "c5"]
    q001_relevant = {"FIBA:41.1"}
    assert reciprocal_rank(q001_ranked, q001_relevant, k=5) == pytest.approx(1 / 3)

    # 2. 1. sırada isabet
    first_hit_ranked = ["FIBA:41.1", "c2", "c3", "c4", "c5"]
    assert reciprocal_rank(first_hit_ranked, q001_relevant, k=5) == 1.0

    # 3. İsabet yok
    no_hit_ranked = ["c1", "c2", "c3"]
    assert reciprocal_rank(no_hit_ranked, q001_relevant, k=3) == 0.0

    # 4. q002 B (Birden fazla relevant var, ilk isabet 2. sırada)
    q002_ranked = ["c1", "IFAB:7.1", "FIBA:8.1", "c4", "c5"]
    q002_relevant = {"IFAB:7.1", "FIBA:8.1"}
    assert reciprocal_rank(q002_ranked, q002_relevant, k=5) == 0.5

    # 5. q001, k=2 (İsabet 3. sırada olduğu için ilk 2'de bulunamıyor)
    assert reciprocal_rank(q001_ranked, q001_relevant, k=2) == 0.0
def test_recall_at_k_invalid_k_raises_value_error():
    ranked = ["c1", "c2", "c3"]
    relevant = {"c1"}

    with pytest.raises(ValueError):
        recall_at_k(ranked, relevant, k=0)


def test_reciprocal_rank_invalid_k_raises_value_error():
    ranked = ["c1", "c2", "c3"]
    relevant = {"c1"}

    with pytest.raises(ValueError):
        reciprocal_rank(ranked, relevant, k=-1)
