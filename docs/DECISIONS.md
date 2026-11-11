# Decisions

## 2026-11-10 — Golden set 50 soruyla başlar

**Status:** Accepted

- **Context:** README 50 soru diyor, rehber 100 öneriyor. 50 soruda tek bir sorunun düşmesi recall@10'u yaklaşık 2 puan oynatır ve "1 puan" eşiğini tek başına aşar.
- **Options:** 50 · 100 · 50 ile başlayıp ölçünce karar vermek
- **Decision:** 50 soruyla başlanacak. Gerekirse CP-05'ten sonra büyütülecek.
- **Rationale:** Takvim sıkışık. Eşiğin gerçek hassasiyeti ölçülmeden 100 soruya emek harcamak tahmine dayanır.
- **Revisit when:** CP-05'te kapı tek soruluk değişimlerde gereksiz yere kırılıyorsa.

## 2026-11-10 — Kapsam: ürün katmanı yok

**Status:** Accepted

- **Context:** Rehberdeki Hybrid RAG projesi API, dashboard, Docker, demo, dedup ve çok formatlı loader da içeriyor. Ship gate bunların hiçbirini istemiyor ve bütçe ~48 saat.
- **Decision:** Bunlar kapsam dışı. LLM-as-judge ile citation doğrulama P2'ye kalıyor. P1'de yalnızca "citation getirilen bir chunk'a işaret ediyor mu?" kontrolü yapılacak.
- **Rationale:** Bütçe ship gate'e harcanmalı. LLM ile doğrulama P2'nin konusuyla çakışıyor.
- **Revisit when:** Ship gate erken kapanırsa.

## 2026-11-10 — CI kapısı baseline'dan hemen sonra

**Status:** Accepted

- **Context:** Rehberde kapı sonda kuruluyor.
- **Decision:** Kapı CP-05'te, dense baseline'dan hemen sonra kurulacak.
- **Rationale:** Hybrid ve reranker kapıdan geçen gerçek değişiklikler olur ve kapı birden fazla kez sınanır.
- **Consequences:** Embedding'lerin CI'da nasıl üretileceği CP-05'te çözülmeli, çünkü GitHub Actions'ta Ollama yok.
