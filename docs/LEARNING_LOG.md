# Learning Log

Kanıta dayanır. Bir konu yalnızca teach-back veya küçük bir varyasyon çözüldüğünde "Passed" olur.

## Entries

### 2026-11-12 — CP-00 Embedding ve kosinüs benzerliği
- **Status:** Passed
- **Kanıt:** Kosinüs `scratch/cosine.py` ile stdlib kullanılarak hesaplandı. Veri şekli hatası (`TypeError: 'float' object is not iterable`) traceback okunarak düzeltildi. Transfer deneyinin beklentisinde "model benzer anlamları yakına koymayı eğitimde öğrenmiş" gerekçesi kendi cümleleriyle yazıldı ve 0.30'luk ilgisiz çift taban olarak kullanıldı.
- **Karışıklıklar:** A, B ve C önce tek sayı sanıldı (cümle → 768'lik vektör, çift → tek skor ayrımı). İlk teach-back'te yakınlığı modelin hesapladığı düşünüldü (oysa model vektörü üretiyor, skoru `cosine` hesaplıyor).
- **Pekiştir:** Boyutun modelden geldiği (768) henüz kendi cümleleriyle açıklanmadı. Cold/warm ayrımı CP-07 gecikme ölçümünde tekrar ele alınacak.

### 2026-11-14 — CP-01 Korpus, BM25 ve golden set etiketi
- **Status:** Passed (2026-11-14, transfer sorusundan sonra)
- **Kanıt (transfer):** Kendi cümleleriyle: chunk boyutu 500'den 300'e inince "c8'in yeri kayıyor ve farklı bir metin gösteriyor". Yeni senaryoda doğru tahmin: retriever 41.1'i taşıyan c10'u getirse bile etiket c8 olduğu için soru "kaçırıldı" sayılır; yani düşüş retriever'dan değil etiketten gelir.
- **Kanıt:** Toy BM25 deneyinde (`scratch/bm25_toy.py`) D3'ün D2'yi geçmesini uzunluk cezasıyla, D1'in birinciliğini "the"nin iki kez geçmesiyle açıklayan doğru hipotez kendi cümleleriyle yazıldı (BUGLOG `[BULGU]`).
- **Karışıklıklar:** A/D cümleleri için BM25'in "1'e yakın" skor vereceği düşünüldü (BM25'i kosinüs gibi 0-1 benzerlik sandı). "Chunk ne oluyordu" sorusu: chunk kavramı tekrar anlatıldı. Etiket birimi ve eşleşme kuralı sorularına "bilmiyorum". Teach-back'te etiketin madde adresi olma nedeni "cevap doğrudan madde adresinde" ve "chunk olunca birden fazla yerde arama gerekmez" diye tahmin edildi; asıl neden (chunk ID'leri chunking değişince değişir, golden set üç stratejide de geçerli kalmalı) söylenmedi.
- **Pekiştir:** "Birlikte tam kapsama"nın neyi ölçtüğü kendi cümleleriyle anlatılmadı. CP-02'de recall@k'yı elle hesaplarken tekrar ele alınacak. BM25 skorunun 0-1 aralığında olmadığı CP-06'da hatırlatılacak.

### 2026-11-15 — CP-02 Metrik çekirdeği (recall@k, MRR, nDCG)
- **Status:** Passed (teach-back + transfer)
- **Kanıt:** `recall_at_k`, `reciprocal_rank`, `ndcg_at_k` kendisi yazdı, 12 test (`tests/test_metrics.py`). Teach-back kendi cümleleriyle: "MRR ile ilk doğru cevap ne kadar yukarda", "nDCG ile bütün doğrular ideale göre ne kadar yukarda". Yeni senaryo `[c1, c2, c3, c4, A]`, etiket {A, B}: recall 0.50, RR 0.20, nDCG 0.24 doğru hesaplandı ve teste çevrildi. Break: IDCG sınırı kaldırılınca yalnızca k=1 testinin neden kırıldığını açıkladı ("1-3'te ikisi de 2, 4'te min 1 len 2").
- **Kanıt (birlikte tam kapsama, CP-01 pekiştirmesi kapandı):** Madde c7/c8'e bölünmüş, yalnızca c7 gelmiş → "bulunmaz, recall 0". Herhangi bir örtüşme kuralında "recall 1 olurdu, LLM maddenin yarısıyla cevap verirdi".
- **Karışıklıklar:** MRR önce doğrusal azalan puan sanıldı. nDCG alıştırmasında IDCG bulunan isabetlerden hesaplandı. Kodda `ideal_isabet = k` ve `range(0, n+1)` (ZeroDivisionError). Negatif slice `ranked[:-1]` son eleman sanıldı. Teach-back'te recall'un "hiç sorun göstermediği" ve RR'ın eksik etiketi gördüğü söylendi; kontrol sorusuyla düzeldi (RR B'nin eksik olduğunu görmez).
- **Pekiştir:** Recall tanımı tek etiketli dille anlatıldı ("ilk k'nın içinde mi"); çok etiketli tanım hesapta doğru. Chunk → etiket dönüşümünde etiketin hangi sırada sayılacağı (kapsamayı tamamlayan son chunk'ın sırası?) CP-03/04'te karara bağlanacak.
