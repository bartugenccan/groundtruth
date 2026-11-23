import pytest

from groundtruth.extract import join_pages


def test_join_pages_records_page_starts():
    # İz tablosundaki örnek: "abc" (3) + "\n" → 4, "defg" (4) + "\n" → 9
    text, page_starts = join_pages(["abc", "defg", "hi"])

    assert text == "abc\ndefg\nhi"
    assert page_starts == [0, 4, 9]


def test_join_pages_single_page():
    # Tek sayfada ayraç yok, sayfa 0'dan başlar
    assert join_pages(["abc"]) == ("abc", [0])


def test_join_pages_empty():
    # Sayfa yoksa başlangıç da yok
    assert join_pages([]) == ("", [])


@pytest.mark.parametrize(
    "pages",
    [
        ["abc", "defg", "hi"],
        ["", "abc", ""],  # boş sayfalar da bir konum kaplar
        ["satır 1\nsatır 2", "x"],  # sayfa içi "\n" konumları bozmamalı
    ],
)
def test_join_pages_starts_point_to_each_page(pages):
    # Değişmez: her başlangıçtan sayfa uzunluğu kadar kesilen metin o sayfanın kendisi
    text, page_starts = join_pages(pages)

    assert len(page_starts) == len(pages)
    assert all(
        text[start : start + len(page)] == page
        for start, page in zip(page_starts, pages)
    )
