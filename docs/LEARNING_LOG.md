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
