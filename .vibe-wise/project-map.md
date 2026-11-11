# Project Map

## Purpose
Bir retrieval değişikliğinin (chunk boyutu, hybrid, reranker) işe yarayıp yaramadığını sayıyla kanıtlayan RAG ve eval harness'i.

## Requirements
- Ship gate: `README.md` (6 madde). Checkpoint'ler: `docs/ROADMAP.md` (CP-00..CP-09).
- Python 3.14, Ollama yerel (`nomic-embed-text`, `qwen3:4b`), ücretli API yok, Guester verisi yok, repo public.
- Kapsam kararları: `docs/DECISIONS.md`.

## Components
Henüz kod yok. Planlanan (ROADMAP): golden set, metrik çekirdeği, ingestion + 3 chunking, dense / BM25 / RRF / reranker, generation + citation, CI kapısı.

## Main Flow
? (CP-01..CP-04'te learner tasarlayacak)

## Data and Trust Boundaries
Korpus: seçilmedi (CP-01). Embedding/generation: yerel Ollama HTTP API.

## Build and Deployment
Doğrulanmış komut yok. `.gitignore`: `.venv/`, `__pycache__/`, `*.pyc`, `.env`.

## Unknowns
Vector store, BM25 kütüphanesi, reranker modeli, golden set etiket birimi, CI'da embedding üretimi (bkz. ROADMAP Risks).
