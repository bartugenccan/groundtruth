from pathlib import Path
from pypdf import PdfReader


def extract_pages(pdf_path: Path) -> list[str]:
    pdf = PdfReader(pdf_path)

    return [p.extract_text() or "" for p in pdf.pages]


def join_pages(pages: list[str]) -> tuple[str, list[int]]:
    page_starts = []

    location = 0

    for page in pages:
        page_starts.append(location)
        location = location + len(page) + 1

    text = "\n".join(pages)

    return (text, page_starts)
