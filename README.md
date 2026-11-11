# groundtruth (P1)

Hybrid RAG ve retrieval eval: bir değişikliğin retrieval'ı iyileştirip iyileştirmediğini görüşle değil, sayıyla kanıtlamak.

**Hafta:** W1-4 (6 Kas–3 Ara) · ~48 saat · **Dil:** Python · **Model:** Ollama (yerel, ücretsiz)
**Rehber:** `../design-cards/sources/P15.pdf` s.16-19 (Hybrid RAG) ve `S6.pdf` s.6 (Groundtruth). Fazlar bu iki rehberden.

## Ship gate (bitti sayılması için)
- [ ] Elle yazılmış en az 50 soruluk golden set: tek kaynaklı, çok kaynaklı, cevabı olmayan, belirsiz
- [ ] 3 konfigürasyon karşılaştırıldı: chunk boyutu, hybrid vs dense, reranker açık/kapalı
- [ ] Sonuç tablosu (recall@k, MRR, nDCG, kategori bazında) ve takası yazılmış bir öneri
- [ ] CI kapısı: recall@10 1 puandan fazla düşerse PR kırılır, bilerek bozulan bir değişiklikle gösterildi
- [ ] Hâlâ başarısız olan 5 sorunun hata analizi
- [ ] README sırası: tek satır sonuç → tablo → diyagram → kararlar → neler çalışmadı

## Adımlar
0. [ ] **Deney (≤1 saat):** Ollama'da bir embedding modeli seç ve doğrula. İki cümlenin embedding'ini al, kosinüs benzerliğini elle hesapla.
1. [ ] Korpus seç (gerçek ve birbirine bağlı dokümanlar, Guester verisi değil) ve golden set'i yaz. Eval özellikten önce gelir.
2. [ ] Ingestion ve 3 chunking stratejisi
3. [ ] Dense arama, BM25, RRF ile birleştirme, ardından reranker
4. [ ] Cevap üretimi, citation doğrulama, "bilmiyorum" durumu
5. [ ] Eval: retrieval metrikleri ile faithfulness ayrı raporlanır
6. [ ] Break: beklentiyi `docs/BUGLOG.md`'ye yaz, sonra kır (chunk boyutu, embedding değişimi, bozuk dosya, cevapsız soru)
7. [ ] CI kapısı ve paketleme

**Bir alt katman:** Index bellekte ne kadar yer tutuyor? Bir sorgunun süresi nerelere gidiyor? Ölç.
