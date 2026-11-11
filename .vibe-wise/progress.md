# Learning Progress

No learning events recorded yet.

## Pending decision
- **CP-01 başlangıcı — next:** BUGLOG tamam ([BULGU] Neden: learner hipotezi). Tweet konuşması ertelendi (learner "sonra"). Commit atıldığı doğrulanmadı. Sıradaki: rehber sayfalarını okuyup korpus seçimi (learner kararı).

## Project overview
- Introduced (2026-11-11): RAG nedir, groundtruth'un ürünü ölçüm düzeneği, planlanan akış (chunking → embedding → arama → LLM → eval → CI kapısı). Learner RAG/retrieval'ı "hiç bilmiyorum" olarak bildirdi.
- Introduced (2026-11-11, diyagramlarla): embedding/vektör/kosinüs sezgisi; projenin tamamı: chunking türleri, dense vs BM25, RRF, reranker (cross-encoder), citation + "bilmiyorum", golden set, recall@k/MRR/nDCG sezgisi, retrieval vs generation hatası, CI kapısı, CP haritası. Henüz demonstrated understanding yok.

## Embedding ve kosinüs (CP-00)
- Introduced: boyut modelden gelir (nomic-embed-text → 768, ölçüldü 2026-11-11); göreli dosya yolu cwd'ye göre çözülür.
- Needs reinforcement (2026-11-12): learner A/B/C'yi tek sayı sandı ("3 sayı alacağız sandım"); cümle → 768'lik vektör, çift → tek skor ayrımı yeniden anlatıldı (diyagramla).
- Debug: `FileNotFoundError` ve `KeyError` (typo) learner tarafından düzeltildi; `TypeError: 'float' object is not iterable` veri şekli hatasından.
- Açık soru: `dot/norm/cosine` fonksiyonlarını learner mı yazdı, bir yerden mi alındı (iki kez soruldu, cevap yok; tekrar ısrar edilmedi).
- 2026-11-12 sonuç: cos(A,B)=0.783, cos(A,C)=0.305, cos(B,C)=0.310; learner beklentisi (A'ya B yakın) tuttu. Vektör normları 1.0 (Claude ölçtü). İlk istekte load_duration 3.72 s / total 3.86 s.
- Introduced: ilgisiz cümle skoru 0 değil (0.31) → eşik mutlak değil; normalize vektörde cos = dot.
- Süre (2026-11-12): cold 4088 ms (load 3979) / warm 38 ms; beklenti önceden yazılmadı. `ollama ps` UNTIL ≈ 3 dk gözledi. Cold/warm kavramı anlatıldı.
- Teach-back (2026-11-12): Doğru: cümle → vektör, kosinüsle yakınlık ölçülür (vektör/sayı karışıklığı giderilmiş görünüyor). Eksik/kayık: "model text'te yakınlığı anlayamıyor" dedi; yakınlığı modelin değil bizim (cosine) hesapladığımız ve modelin anlamca yakını yakın vektöre koyacak şekilde eğitildiği söylenmedi; 768'in modelden geldiği söylenmedi. Learning: Needs reinforcement → transfer deneyi (D cümlesi) önerildi.
- Transfer (2026-11-12): Learner beklentisi "eğitimde benzer anlamları yakına koymayı öğrendi" + 0.30 tabanını kullanarak D için ~0.70 tahmin etti (demonstrated reasoning). Ölçüm cos(A,D)=0.959 > cos(A,B)=0.783 → bulgu adayı. CP-00 Learning: Passed.
