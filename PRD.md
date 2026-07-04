# PRD: Sağlık Turizmi & Seyahat AI Ajanı (HealRoute AI)

**Durum:** Finalize Edilmiş Plan
**Hazırlayan:** Ali Erkin Avcı & Ekip Arkadaşları
**Tarih:** 4 Temmuz 2026
**Versiyon:** 1.0

---

## 1. Özet (TL;DR)

Kullanıcının doğal dille ifade ettiği bir sağlık/estetik ihtiyacını ("dişimi yaptırmak istiyorum", "botoks olmak istiyorum") uçtan uca bir seyahat + tedavi planına dönüştüren, bunu rezervasyona kadar taşıyan bir AI ajanı (HealRoute AI). Sistem hem klinik/işlem önerisi yapar hem de bu işlemi bir tatil planına oturtur (uçak, otel, güzergah, yerel danışmanlık dahil). Gelir modeli klinik komisyonu üzerinden kurulur.

Kısaca: **sağlık turizmi ajansı + seyahat danışmanı rolünü tek bir sohbet arayüzüne sıkıştırmak.**

---

## 2. Problem Tanımı

### 2.1 Bugünün deneyimi neden kötü?
- Sağlık turizmi süreci parçalı: hasta önce kliniği bulur (genelde bir aracı ajans üzerinden, düşük şeffaflık, yüksek komisyon), sonra ayrı ayrı uçak/otel ayarlar, sonra yerelde kendi başına kalır (ulaşım, fiyat pazarlığı, dil bariyeri).
- Aracı ajanslar genelde tek bir kliniğe/pakete kilitlidir; kullanıcı gerçek anlamda karşılaştırma yapamaz.
- **Kısıtlı Paket Yapısı ve Şeffaflık Eksikliği:** Bazı turizm acenteleri veya doğrudan hizmeti sunan dişçiler/klinikler benzer tatil + tedavi paketleri sunmaktadır. Ancak bu çözümler yalnızca kendi kliniklerini veya sınırlı partnerliklerini kapsadığı için kullanıcılara şeffaf bir karşılaştırma imkanı sunmamakta, kullanıcıları tek bir kliniğe mahkum etmektedir.
- Yerli kullanıcı için de (örn. İstanbul'da yaşayan biri Muğla'da bir işlem yaptırmak istediğinde) benzer parçalılık var — sadece "yurt dışı" değil, şehirlerarası sağlık + seyahat kombinasyonu da aynı sürtünmeyi yaşıyor.
- Karar verme yükü kullanıcıda: hangi klinik güvenilir, fiyat makul mü, tatili nasıl kurgularım, yerelde nasıl davranırım (taksi ücreti, hangi bölgede kalınır vs.) — hepsi dağınık kaynaklardan toplanıyor.

### 2.2 Neden şimdi?
- LLM tabanlı sohbet arayüzleri (Claude/ChatGPT tarzı) kullanıcı davranışını değiştirdi: insanlar artık karmaşık, çok adımlı planlama işlerini doğal dille bir ajana devretmeye alışıyor.
- Türkiye sağlık turizminde zaten güçlü bir arz tarafı var (klinik yoğunluğu, fiyat avantajı, uluslararası talep) — eksik olan talep tarafındaki sürtünmeyi azaltan akıllı katman.

---

## 3. Hedefler ve Başarı Kriterleri

### 3.1 Ürün hedefleri
1. Kullanıcının tek bir doğal dil girdisinden (ör. "botoks olmak istiyorum") uçtan uca bir plan (klinik önerisi + seyahat planı) üretmek.
2. Bu planı sadece öneri olarak değil, **uygulanabilir** (rezerve edilebilir) hale getirmek.
3. Klinik tarafında komisyon bazlı, sürdürülebilir bir gelir modeli kurmak.

### 3.2 İş hedefleri
- Pilot bölge olarak **Muğla (Bodrum, Fethiye)** ve **İstanbul** seçilmiştir. İşlem kategorilerinde ise yüksek hacimli olan **Diş (implant, beyazlatma)** ve **Estetik (botoks, dolgu)** alanlarına odaklanılacaktır.
- Pilot dönem boyunca sisteme en az 10 partner klinik dahil edilmesi ve ilk pilot kullanıcı testlerinin başarıyla tamamlanması hedeflenmektedir.

### 3.3 Başarı metrikleri
- Sohbetten gerçek rezervasyona (deep-link yönlendirmesine) dönüşüm oranı.
- Klinik başına ortalama komisyon geliri.
- Kullanıcı memnuniyeti / NPS (özellikle yerel rehberlik, taksi ve güzergah tavsiyeleri için).
- Tekrar kullanım oranı (özellikle yerli kullanıcı segmentinde).

---

## 4. Hedef Kitle

| Segment | Tanım | Temel ihtiyaç |
|---|---|---|
| Yabancı sağlık turisti | Yurt dışından Türkiye'ye işlem için gelen kişi | Güvenilir klinik + tatil kombinasyonu + dil/lojistik desteği |
| Yerli kullanıcı | Türkiye içinde yaşayan, başka bir şehirde işlem yaptırmak isteyen kişi | Klinik keşfi + seyahat planlaması + yerel bilgi (fiyat, ulaşım) |

**Not:** MVP kapsamında hem yerli hem de yabancı kullanıcı segmentleri desteklenecektir. Dil desteği olarak ilk aşamada Türkçe ve İngilizce sunulacaktır.

---

## 5. Kullanıcı Yolculuğu (Uçtan Uca Akış)

1. **Giriş:** Kullanıcı sade bir sohbet ekranında derdini doğal dille anlatır. ("Dişimi yaptırmak istiyorum", "Botoks olmak istiyorum")
2. **Bilgi toplama (AI tarafından):** Sistem gerekli detayları sorar — işlem türü, bütçe aralığı, tarih esnekliği, tercih edilen bölge, tatil beklentisi (deniz mi, şehir mi), kaç kişi seyahat edecek vb.
3. **Öneri üretimi:** Sistem hem işlem hem tatil planını birlikte sunar. Örnek çıktı formatı:
   - Önerilen bölge (Muğla veya İstanbul) ve neden.
   - Önerilen klinik(ler) — kısa gerekçe ve şeffaf fiyat bilgisi ile.
   - Tatil senaryosu (nerede kalınacak, ne yapılacak).
   - Tahmini toplam bütçe.
4. **Detaylandırma / uygulamaya geçiş:** Kullanıcı planı onaylarsa sistem:
   - Uçak/otel seçeneklerini sunar ve Booking.com & Skyscanner deep-link'leri üzerinden rezervasyonu başlatır.
   - Gün gün program çıkarır (hangi gün nerede kalınacak, işlem günü ne zaman).
   - Rezervasyon tutarını netleştirir.
5. **Seyahat sırasında danışmanlık:** Sistem yerinde/anlık destek verir (ör. "taksi ücreti şu kadar olmalı, fazlasını verme", öneri restoranlar, işlem öncesi/sonrası dikkat edilmesi gerekenler).
6. **İşlem sonrası:** Takip mesajları, memnuniyet anketi, tekrar kullanım teşviki.

---

## 6. Kapsam

### 6.1 MVP Kapsamı
- Tek bir sohbet arayüzü (metin tabanlı).
- Sınırlı sayıda işlem kategorisi (diş + estetik).
- Sınırlı sayıda partner klinik (pilot bölge: Muğla ve İstanbul).
- Temel seyahat planlama (Skyscanner ve Booking.com deep-link yönlendirmeli rezervasyon).
- Basit bir "yol boyunca danışmanlık" katmanı (statik bilgi + sohbet üzerinden soru-cevap; ilk aşamada gerçek zamanlı GPS konum takibi MVP dışıdır).

### 6.2 MVP Dışı / Sonraki Fazlar
- Çok dilli, çok segmentli tam otomasyon.
- Gerçek zamanlı seyahat asistanlığı (konum bazlı, proaktif bildirimler).
- Klinik tarafında self-servis partner paneli.
- Ödeme/finansal aracılık (escrow, taksitlendirme vb.).
- Mobil uygulama (Android & iOS).

---

## 7. Temel Özellikler (Fonksiyonel Gereksinimler)

| # | Özellik | Açıklama | Öncelik |
|---|---|---|---|
| 1 | Doğal dil ile ihtiyaç toplama | Kullanıcının serbest metin girdisinden işlem türünü, tercihlerini çıkarma | Yüksek |
| 2 | Klinik eşleştirme motoru | İşlem + bölge + bütçeye göre klinik önerisi | Yüksek |
| 3 | Seyahat planı üretimi | Klinik lokasyonuna göre tatil/konaklama önerisi | Yüksek |
| 4 | Rezervasyon entegrasyonu | Uçak/otel seçimi ve Booking/Skyscanner deep-link yönlendirmesi | Yüksek |
| 5 | Yerinde danışmanlık | Fiyat/ulaşım/lojistik konularında anlık tavsiye | Orta |
| 6 | Klinik komisyon takibi | Hangi rezervasyonun hangi klinikten geldiğinin izlenmesi | Yüksek |
| 7 | Yasal Uyarı Sorumluluk Sınırı | Tıbbi tavsiye verilmediğini belirten açık uyarılar (disclaimer) | Yüksek |

---

## 8. Gelir Modeli

- **Klinik Komisyonları:** Platform üzerinden yönlendirilen ve gerçekleşen tedaviler için kliniklerden alınacak %10-%15 arası komisyon geliri.
- **Affiliate (Ortaklık) Gelirleri:** Booking.com, Skyscanner ve yerel transfer firmalarına yönlendirilen trafikten elde edilecek komisyonlar.
- **Kullanıcı Ücretlendirmesi:** Kullanıcılardan herhangi bir servis veya danışmanlık ücreti alınmayacaktır.

---

## 9. Riskler ve Açık Sorular

### 9.1 İş riskleri
- **Güven/regülasyon:** Sağlık turizmi regüle bir alan; klinik önerilerinin tıbbi tavsiye sınırına girmemesi, gerekli izin/lisans süreçlerinin netleştirilmesi gerekiyor.
- **Klinik tarafı satışı:** Komisyon modeli için yeterli sayıda kaliteli klinik partnerliği kurmak zaman ve güven ister — soğuk başlangıç problemi.
- **Sorumluluk sınırı:** İşlem sırasında/sonrasında bir sorun olursa (tıbbi komplikasyon, iptal, memnuniyetsizlik) platformun sorumluluğu nerede başlıyor/bitiyor?

### 9.2 Ürün riskleri
- **Kullanıcı güveni:** "Bu öneri gerçekten bana mı uygun, yoksa komisyon en yüksek olan mı öne çıkıyor?" algısı yönetilmeli — öneri motorunun şeffaflığı önemli.
- **Tıbbi Ciddiyet Ayrımı:** Doğal dil girdisinin tıbbi ciddiyet taşıyan acil durumlarla karışması durumunda sistemin ne zaman durması gerektiği tanımlanmalı ve yasal uyarılar net gösterilmelidir.

### 9.3 Karara Bağlanan Sorular
1. **İlk pilot hangi şehir/bölge ve hangi işlem kategorisiyle başlayacak?** Muğla (Bodrum/Fethiye) ve İstanbul pilot bölgelerinde Diş ve Estetik kategorileriyle.
2. **Hedef kitlede önce yabancı mı yerli kullanıcı mı önceliklendirilecek?** MVP'de her iki segment de (Türkçe ve İngilizce dillerinde) desteklenecektir.
3. **Klinik partnerlikleri nasıl kurulacak?** Mevcut klinik ağları ve özel anlaşmalar üzerinden başlanacaktır.
4. **Rezervasyon tarafı kendi entegrasyonumuz mu olacak?** Booking.com ve Skyscanner deep-link'leri kullanılarak entegrasyon yükü azaltılacaktır.
5. **Yasal/regülasyon açısından sağlık turizmi aracılığı için gereken izinler neler?** Tıbbi yönlendirme yapılmadığı belirtilerek sadece seyahat ve alternatif klinik listeleme hizmeti sunulacaktır.

---

## 10. Rakip / Referans Alan Taraması

- **Geleneksel Sağlık Turizmi Acenteleri:** Genellikle manuel telefon/WhatsApp görüşmeleri ile tek bir kliniğe yönlendirme yaparlar.
- **Genel AI Seyahat Planlayıcıları (örn. Roam Around, Layla):** Genel turistik seyahat planlarlar ancak klinik seçimi ve tedavi sonrası bakım lojistiği sunmazlar.
- **HealRoute AI Farkı:** Sağlık ihtiyaçları ile seyahat planlamasını akıllıca eşleştiren tek dikey yapay zeka asistanıdır.

---

## 11. Sonraki Adımlar

1. Takım içi rollerin ve takım isminin netleştirilerek README.md'ye işlenmesi.
2. Teknik mimari tasarımı ve Gemini API bağlantılarının kodlanması.
3. Muğla ve İstanbul bölgelerindeki mock klinik veritabanının JSON/Veritabanı formatında hazırlanması.
