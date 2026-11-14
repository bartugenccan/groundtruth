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

## 2026-11-12 — Korpus: futbol ve basketbol kural kitapları

**Status:** Accepted. Dil: İngilizce doküman ve sorular (learner kararı, gerekçe belirtilmedi). Sürüm önerisi: IFAB 2026/27 + FIBA 2026 v1.1 (resmi URL'ler 2026-11-12'de PDF döndü). Kullanıcı senaryosu açık.

- **Context:** CP-01 korpusu birbirine bağlı, sınırı net ve tam terim içeren dokümanlar istiyor. Golden set'in cevaplarını insan doğrulamalı.
- **Options:** PostgreSQL docs · Kubernetes docs · GDPR + EDPB · futbol/basketbol kural kitapları (IFAB Laws of the Game + FIBA Official Basketball Rules) · futbol/basketbol Wikipedia makaleleri
- **Decision:** Kural kitapları (IFAB + FIBA).
- **Rationale:** "Seçenek A benim için uygundur. 50'sini de doğrularım." (learner)
- **Consequences:** İki metin de telifli, yeniden dağıtım izni yok (IFAB ve FIBA notları, 2026-11-12 aramasıyla). Metin repoya girmez, resmi kaynaktan indiren script olur. Kaynaklar PDF; PDF loader kapsam dışıydı, bu çelişki çözülmeli.
- **Revisit when:** Resmi PDF'lerden temiz metin çıkarılamazsa.

## 2026-11-12 — Golden set soruları Claude taslağı, insan doğrulaması

**Status:** Accepted

- **Context:** README ship gate "elle yazılmış" diyordu. Rehber (S6) insanın gözden geçirdiği, modelin tek seferde uydurmadığı bir set istiyor. Learner 50 soruyu kendisi yazmak istemedi, iki sporu da bildiğini söyledi.
- **Options:** Hibrit + köken alanı · hepsini Claude yazar, learner inceler · hepsini learner yazar
- **Decision:** Hepsini Claude yazar, learner her birini PDF'e karşı inceler.
- **Rationale:** "Anlamsız bir iş olur benim yazmam, sen yaz ben incelerim, bu iki sporun da her şeyini biliyorum." (learner)
- **Consequences:** README ship gate ifadesi güncellendi. Bilinen sınır: model yazımı sorular metnin kelimelerine yakın olabilir, BM25 ve recall'u şişirebilir. Bu, README'nin "neler çalışmadı" bölümüne yazılacak.
- **Revisit when:** İncelemede soruların çoğu düzeltme gerektirirse.

## 2026-11-12 — Etiket birimi ve eşleşme kuralı

**Status:** Accepted

- **Context:** Chunk ID'leri chunking stratejisine göre değişir. Golden set üç stratejide de geçerli kalmalı (ROADMAP riski "Etiket birimi").
- **Options:** Tam içerme (learner'ın ilk seçimi) · herhangi bir örtüşme · eşikli örtüşme · birlikte tam kapsama
- **Decision:** Etiket, kural kitabının en küçük alt madde adresi (`FIBA:41.1`, `IFAB:7.1`). Çok kaynaklı soruda birden fazla adres, cevapsız soruda boş liste. Eşleşme kuralı "birlikte tam kapsama": ilk k chunk etiketlenen maddenin tamamını birlikte kapsıyorsa bulundu. Çok kaynaklıda her adres ayrı ayrı kapsanmalı. Kuralın tanımı README'ye yazılır.
- **Rationale:** Claude'un önerisi, learner onayladı (learner kendi gerekçesini yazmadı). Tam içerme, FIBA'da alt maddelerin ~%17'si 500 karakteri aştığı (kaba regex ölçümü) ve 229 karakterlik medyan bir maddenin 500'lük sabit chunk'a sığma olasılığı ~%54 olduğu için sabit boyutlu chunking'i kural yüzünden cezalandırırdı.
- **Consequences:** CP-03'te chunk metadata'sı ve golden set etiketleri kaynak metindeki karakter konumlarına eşlenebilmeli. "Kısmi" kapsama (çok kaynaklıda tek adres bulunması) CP-02'de karara bağlanacak.
- **Revisit when:** Karakter konumu eşlemesi PDF metin çıkarma yüzünden güvenilmez olursa.

## 2026-11-14 — Law önsözü için adres kuralı

**Status:** Accepted

- **Context:** Bazı IFAB kuralları numaralı bir bölümde değil, Law'un giriş metninde (1. bölümden önce) duruyor. Örnek: "A goal cannot be scored directly from a throw-in" Law 15'in başında.
- **Decision:** Önsöz metni bölüm numarasız adresle etiketlenir: `IFAB:15`, `IFAB:14`, `IFAB:6`. `IFAB:15` yalnızca önsözü gösterir, Law 15'in tamamını değil.
- **Rationale:** Claude'un önerisi, learner onayladı ("Decisions'a yazabilirsin").
- **Consequences:** CP-03'te önsöz metninin karakter aralığı, Law başlığı ile ilk numaralı bölüm arasındaki metin olarak çıkarılmalı.
