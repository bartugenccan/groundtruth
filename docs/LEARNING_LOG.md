# Learning Log

Kanıta dayanır. Bir konu yalnızca teach-back veya küçük bir varyasyon çözüldüğünde "Passed" olur.

## Entries

### 2026-11-12 — CP-00 Embedding ve kosinüs benzerliği
- **Status:** Passed
- **Kanıt:** Kosinüs `scratch/cosine.py` ile stdlib kullanılarak hesaplandı. Veri şekli hatası (`TypeError: 'float' object is not iterable`) traceback okunarak düzeltildi. Transfer deneyinin beklentisinde "model benzer anlamları yakına koymayı eğitimde öğrenmiş" gerekçesi kendi cümleleriyle yazıldı ve 0.30'luk ilgisiz çift taban olarak kullanıldı.
- **Karışıklıklar:** A, B ve C önce tek sayı sanıldı (cümle → 768'lik vektör, çift → tek skor ayrımı). İlk teach-back'te yakınlığı modelin hesapladığı düşünüldü (oysa model vektörü üretiyor, skoru `cosine` hesaplıyor).
- **Pekiştir:** Boyutun modelden geldiği (768) henüz kendi cümleleriyle açıklanmadı. Cold/warm ayrımı CP-07 gecikme ölçümünde tekrar ele alınacak.
