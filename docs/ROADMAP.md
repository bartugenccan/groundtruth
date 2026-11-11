# ROADMAP: groundtruth (P1)

> **Durum: Onaylandı (2026-11-10).** Kararlar: [DECISIONS.md](DECISIONS.md).

## Project
- **Purpose:** Bir retrieval değişikliğinin (chunk boyutu, hybrid, reranker) işe yarayıp yaramadığını sayıyla kanıtlayan bir RAG ve eval harness'i.
- **Target outcome:** README'deki ship gate'in altı maddesi kanıtla kapanmış olmalı.
- **Current state:** 2026-11-10 itibarıyla kod yok, commit yok. `docs/BUGLOG.md` boş. Ollama'da `nomic-embed-text` ve `qwen3:4b` kurulu.
- **Stack / runtime:** Python 3.14, Ollama (yerel embedding ve üretim), pytest. Vector store, BM25 kütüphanesi ve reranker kararları ilgili checkpoint'te verilecek.
- **Constraints:** ~48 saat, bitiş 3 Aralık. GTX 1080 Ti 11 GB, 16 GB RAM. Ücretli API yok. Guester verisi yok. Repo public olacak.
- **Out of scope:** FastAPI servisi, dashboard, Docker, demo videosu, near-duplicate tespiti ve PDF/HTML loader'ı. LLM-as-judge ile citation doğrulama P2 judge-gate'e kaldı. P1'de citation'ın getirilen chunk'lardan birine işaret ettiği deterministik olarak kontrol edilir.

## Learning objectives
- Embedding ve kosinüs benzerliğini elle hesaplayıp açıklayabilmek.
- recall@k, MRR ve nDCG'yi elle hesaplamak ve hangisinin hangi soruya cevap verdiğini söylemek.
- Dense, BM25, RRF ve cross-encoder reranker'ın ne zaman kazanıp ne zaman kaybettiğini kanıtla göstermek.
- Retrieval hatasını generation hatasından ayırmak (faithfulness ayrı raporlanır).
- Küçük bir eval setinde regresyon eşiğinin istatistiksel sınırını bilmek.

## Checkpoints

| ID | Checkpoint | Outcome | Dependencies | ~Saat | Implementation | Learning |
|---|---|---|---|---|---|---|
| CP-00 | Embedding deneyi | İki cümlenin embedding'i alınmış, kosinüs elle hesaplanmış, boyut ve süre ölçülmüş | — | 1 | Done | Passed |
| CP-01 | Korpus ve golden set v1 | Korpus seçilmiş, gerekçesi yazılmış. 50+ soru 4 kategoride, chunk'tan bağımsız etiketli, versiyonlu dosyada | CP-00 | 7 | Not started | Not assessed |
| CP-02 | Metrik çekirdeği | recall@k, MRR, nDCG fonksiyonları, elle hesaplanmış örneklere karşı pytest ile doğrulanmış | CP-01 | 3 | Not started | Not assessed |
| CP-03 | Ingestion ve 3 chunking | Sabit boyut, yapıya duyarlı ve semantic chunking seçilebilir. Chunk metadata'sı golden set etiketine eşlenebiliyor | CP-01 | 6 | Not started | Not assessed |
| CP-04 | Dense baseline | Uçtan uca ilk sonuç satırı: dense × 3 chunking, kategori bazında metrikler | CP-02, CP-03 | 4 | Not started | Not assessed |
| CP-05 | CI kapısı | recall@10 baseline'dan 1 puandan fazla düşerse kırmızı. Bilerek bozulan bir değişiklikle kırmızı yandığı gösterilmiş | CP-04 | 4 | Not started | Not assessed |
| CP-06 | BM25 ve RRF hybrid | Hybrid ve dense karşılaştırması tabloda, kapıdan geçen bir değişiklik olarak | CP-05 | 4 | Not started | Not assessed |
| CP-07 | Reranker | Reranker açık/kapalı, kalite ve gecikme birlikte ölçülmüş | CP-06 | 5 | Not started | Not assessed |
| CP-08 | Generation, citation, "bilmiyorum" | Citation'lı cevap, cevapsız sorularda yapılandırılmış ret. Faithfulness ve answer relevance retrieval'dan ayrı raporlanıyor | CP-07 | 6 | Not started | Not assessed |
| CP-09 | Rapor ve hata analizi | Sonuç tablosu, takası yazılmış öneri, hâlâ başarısız 5 sorunun nedeni | CP-08 | 4 | Not started | Not assessed |

Ship gate eşlemesi: golden set → CP-01 · 3 konfigürasyon → CP-04/06/07 · tablo ve öneri → CP-09 · CI kapısı → CP-05 · 5 soru analizi → CP-09 · README → CP-09 sonrası paketleme.

Break her checkpoint'in içinde yapılır, ayrı bir faz değildir. Beklenti önce `docs/BUGLOG.md`'ye yazılır.

## Sıralama gerekçesi
- **Eval önce gelir.** Golden set ve metrikler (CP-01, CP-02) retrieval kodundan önce yazılır. Böylece ilk retrieval satırı yazıldığında ölçülebilir olur.
- **CI kapısı erken.** Rehberde sonda duruyor. Burada baseline'dan hemen sonra geliyor, böylece hybrid ve reranker kapıdan geçen gerçek değişiklikler olur.

## Risks and open questions
- **Takvim:** W1 neredeyse bitti ve henüz commit yok. Kalan ~23 gün içinde yaklaşık 44 saat iş var.
- **Golden set boyutu:** 50 soruyla başlanacak. 50 soruda tek bir sorunun düşmesi recall@10'u yaklaşık 2 puan oynatabilir. CP-05'te eşiğin hassasiyeti ölçülecek, gerekirse set büyütülecek.
- **Etiket birimi:** Chunking değişince chunk ID'leri de değişir. Golden set neye göre etiketlenecek? Tasarım sorusu olarak CP-01'de sorulacak.
- **CI'da Ollama:** GitHub Actions'ta embedding nasıl üretilecek (önbellek, sabitlenmiş sonuçlar, yerel hook)? CP-05'te karar verilecek.
- **Donanım ve sürüm:** Reranker modelinin 1080 Ti'da ve Python 3.14 ile çalıştığı doğrulanmadı. Ollama'nın rerank desteği de doğrulanmadı. CP-07'den önce küçük bir deneyle doğrulanacak.
- **Korpus:** Rehber somut bir kullanım senaryosunun akılda kaldığını söylüyor. Korpus seçimi ve senaryo senin kararın.

## Progress notes
- 2026-11-10: Roadmap taslağı rehberden (S6 #04, P15 #6) ve README'den çıkarıldı ve onaylandı. Sıradaki: CP-00.
- 2026-11-12: CP-00 bitti. nomic-embed-text: 768 boyut, normalize vektörler (norm 1.0), cold ~4 s / warm 38 ms. cos(A,B)=0.78, cos(A,C)=0.31, aynı kelimeler ve farklı anlamla cos(A,D)=0.96 (bulgu adayı, BUGLOG). Sıradaki: CP-01.
