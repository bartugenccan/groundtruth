# groundtruth (P1)

Hybrid RAG and retrieval evaluation: prove with numbers, not impressions, whether a change makes retrieval better.

**Timeline:** W1–4 (Nov 6 – Dec 3) · ~48 hours · **Language:** Python · **Models:** Ollama (local, free)

> Working notes in `docs/` (roadmap, decisions, bug log) are written in Turkish.

## Ship gate (definition of done)
- [ ] Golden set of at least 50 questions (drafted by Claude, every question verified by a human against the source PDF): single-source, multi-source, unanswerable, ambiguous
- [ ] 3 configurations compared: chunk size, hybrid vs. dense, reranker on/off
- [ ] Results table (recall@k, MRR, nDCG, per category) and a recommendation with its trade-offs spelled out
- [ ] CI gate: a PR fails if recall@10 drops by more than 1 point, demonstrated with a deliberately broken change
- [ ] Error analysis of the 5 questions that still fail
- [ ] README order: one-line result → table → diagram → decisions → what didn't work

## Steps
0. [ ] **Experiment (≤1 hour):** Pick an embedding model in Ollama and verify it. Embed two sentences and compute their cosine similarity by hand.
1. [ ] Pick a corpus (real, interlinked documents) and write the golden set. Evaluation comes before features.
2. [ ] Ingestion and 3 chunking strategies
3. [ ] Dense search, BM25, fusion with RRF, then a reranker
4. [ ] Answer generation, citation verification, "I don't know" handling
5. [ ] Eval: retrieval metrics and faithfulness reported separately
6. [ ] Break: write the expectation in `docs/BUGLOG.md` first, then break it (chunk size, embedding change, corrupted file, unanswerable question)
7. [ ] CI gate and packaging

**One layer down:** How much memory does the index take? Where does a query's time go? Measure it.
