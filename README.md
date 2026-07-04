# HealRoute AI: Yapay Zeka Destekli Sağlık Turizmi ve Seyahat Planlama Platformu

> Bu README, YZTA Bootcamp 2026 kapsamında GitHub reposunda bulunması beklenen zorunlu bilgileri ve ürünün detaylı gereksinimlerini içerir.

---

## 📌 Takım İsmi

Grup 27

---

## 👥 Takım Rolleri

| İsim | Rol |
|---|---|
| Selin Küçükterzi | Product Owner / Developer |
| Mahmut Enes Çevik | Scrum Master / Developer |
| Kerem Özdemir | Developer |
| Ali Erkin Avcı | Developer |

---

## 🎯 Ürün İsmi

**HealRoute AI** (Yapay Zeka Destekli Sağlık Turizmi ve Seyahat Planlayıcısı)

---

## 📝 Ürün Açıklaması

HealRoute AI, kullanıcıların doğal dille belirttikleri tedavi ve estetik ihtiyaçlarını (örneğin: *"Bodrum'da diş implantı yaptırmak ve 5 gün tatil yapmak istiyorum"*) analiz ederek, onlara uçtan uca kişiselleştirilmiş bir tedavi planı, klinik önerileri, konaklama, uçuş ve gün gün seyahat rotası sunan akıllı bir asistandır. Platform, hem sağlık turistlerinin klinik arayışındaki şeffaflık sorununu çözer hem de seyahat lojistiğini tek bir sohbet arayüzünde birleştirir.

### Çözülen Temel Problemler:
1. **Sürecin Parçalı Olması:** Hastaların klinik bulma, otel/uçuş ayarlama ve yerel ulaşım/rehberlik ihtiyaçlarını ayrı kanallardan çözmek zorunda kalmasının yarattığı zaman kaybı ve sürtünme.
2. **Şeffaflık Eksikliği ve Tekelci Paketler:** Mevcut sağlık turizmi acentelerinin veya doğrudan hizmeti sunan kliniklerin (örneğin diş klinikleri) yalnızca kendi bünyelerindeki veya anlaşmalı oldukları tekil yerleri kapsayan kapalı paketler sunması; bu durumun pazardaki şeffaf fiyat/kalite karşılaştırma imkanını ortadan kaldırması.
3. **Yerel Lojistik Zorluklar:** Yabancı ve şehir dışından gelen yerli hastaların taksi fiyatları, dil bariyeri, tedavi sonrası bakım süreçleri ve güzergah planlamasında yaşadığı güvensizlikler.

---

## ⚙️ Ürün Özellikleri

- **Doğal Dil ile İhtiyaç Analizi:** LLM tabanlı sohbet arayüzü ile kullanıcının tedavi, bütçe, lokasyon ve tatil tercihlerini toplama.
- **Akıllı Klinik Eşleştirme Motoru:** Tedavi türüne, hedeflenen bütçeye ve uzmanlık puanlarına göre en uygun partner klinikleri önerme.
- **Dinamik Seyahat ve Tatil Planlayıcı:** Seçilen kliniğin konumuna yakın otel, uçuş ve yerel aktivite rotaları oluşturma.
- **Yol Boyu Danışmanlık ve Lojistik Desteği:** Yerel taksi ücretleri, restoran önerileri, dil bariyerini aşacak kelime kartları ve operasyon sonrası bakım yönergeleri sağlama.
- **Şeffaf Fiyatlandırma ve Komisyon Takibi:** Kullanıcıya tüm bütçeyi kırılımlarıyla sunma ve arka planda ortak klinik komisyonlarını takip etme.
- **Yasal Sorumluluk Sınırı (Disclaimer):** Tıbbi tavsiye verilmediğini belirten net uyarı katmanı.

---

## 🎯 Hedef Kitle

| Segment | Tanım | Temel İhtiyaç |
|---|---|---|
| **Yabancı Sağlık Turisti** | Yurt dışından Türkiye'ye işlem için gelen kişi | Güvenilir klinik + tatil kombinasyonu + dil/lojistik desteği |
| **Yerli Kullanıcı** | Türkiye içinde yaşayan, başka bir şehirde (örn. Muğla, Antalya, İstanbul) işlem yaptırmak isteyen kişi | Klinik keşfi + seyahat planlaması + yerel bilgi (fiyat, ulaşım) |

---

## 📋 Product Backlog

🔗 [Backlog Board Linki (Miro / GitHub Projects / Trello) Buraya Eklenecektir](#)

---

## 🚀 Kullanılan Teknolojiler

- **Frontend/Arayüz:** React / Next.js veya Jetpack Compose (Android)
- **Backend / API:** Python (FastAPI) veya Node.js
- **Yapay Zeka:** Gemini 1.5 Pro / Flash API, LangChain veya Vercel AI SDK
- **Veritabanı:** PostgreSQL / Supabase veya MongoDB

---

## 🖥️ Ürün Durumu / Demo

🔗 [Canlı Demo Linki](#) *(Geliştirme aşamasında)*

---

## 🎥 Proje Sunum Videosu

🔗 [YouTube Video Linki](#) *(Sprint 3 sonunda eklenecektir)*

---

## 📅 Sprint Kayıtları

### Sprint 1

**Tarih Aralığı:** 29 Haziran 2026 – 04 Temmuz 2026

**Backlog Düzeni ve Story Seçimleri**
Bu sprintte projenin temel yapay zeka planlama motorunu ve veri katmanını kurmayı hedefliyoruz:
- [x] Proje gereksinimlerinin analiz edilmesi ve PRD'nin son haline getirilmesi.
- [x] Teknik mimarinin (Frontend & AI Backend) kurulması ve API anahtarlarının tanımlanması.
- [x] Pilot bölge olarak **Muğla (Bodrum/Fethiye)** için mock klinik ve otel veritabanının tasarlanması.
- [x] Gemini API entegrasyonu ile ilk metin tabanlı sohbet asistanının (System Prompt + RAG) ayağa kaldırılması.

**Daily Scrum Notları**
- **29 Haziran Pazartesi:** Google AI Akademi, T3 Vakfı ve Sanayi Bakanlığı vizyonuna uygun katma değerli proje fikirleri havuzda toplandı. Adaylar arasında akıllı tarım, afet yönetimi koordinasyonu, KOBİ teşvik navigatörü, sağlık asistanı ve sağlık turizmi planlayıcısı bulunuyor.
- **30 Haziran Salı:** Fikirler elendi ve iki seçeneğe düşürüldü: "KOBİ'ler için KOSGEB/TÜBİTAK/Bakanlık Teşvik Navigatörü" ve "Sağlık Turizmi & Seyahat Planlama Ajanı". İki fikir arasında gidip gelindiği için detaylı araştırma yapılması kararlaştırıldı.
- **1 Temmuz Çarşamba:** Her iki fikrin pazar büyüklükleri ve teknik uygulanabilirlikleri kıyaslandı. KOBİ teşviklerinin veriye erişim zorlukları tartışıldı.
- **2 Temmuz Perşembe:** "Sağlık Turizmi & Seyahat Planlama Ajanı (HealRoute AI)" projesinde nihai karar kılındı. Bu seçimin en önemli nedenleri: Sağlık turizminin Türkiye için yüksek döviz girdisi sağlayan stratejik bir sektör olması ve mevcut acentelerin ya da doğrudan hizmeti sunan dişçilerin/kliniklerin sadece kendi kapalı paketlerini sunarak pazarda yarattığı tekelcilik ve şeffaflık sorununu çözme potansiyelidir.
- **3 Temmuz Cuma:** Ürünün kapsamı (MVP sınırları: Muğla ve İstanbul, Diş ve Estetik tedavileri) netleştirildi ve PRD dokümanı tamamlandı.
- **4 Temmuz Cumartesi:** Sprint 1 başarıyla tamamlandı. `PRD.md` ve `README.md` dosyaları güncellenip finalize edildi, Gemini API entegrasyonu ve mock veritabanı şemaları oluşturuldu.

**Sprint Board Güncellemesi**
- Proje takibi için GitHub Projects panosu aktif olarak kullanılmaktadır. İlgili görevlerin durumları (To Do, In Progress, Done) düzenli olarak güncellenmektedir.

**Ürün Durumu**
- Gemini API ile entegre, terminal üzerinden çalışan ilk çalışan prototip (PoC) tamamlandı. Pilot bölge ve tedavi verileri mock JSON formatında sisteme bağlandı.

**Sprint Review**
- **Tamamlanan İşler:** Fikir seçimi yapıldı, PRD.md hazırlandı, Gemini API entegrasyonu sağlandı ve ilk mock veri kümesi oluşturuldu. Sprint hedeflerinin %100'ü başarıyla tamamlandı.

**Sprint Retrospective**
- **Neyin İyi Gittiği:** Takım içi karar alma süreci hızlı ve yapıcı ilerledi. Teknik altyapı ve AI entegrasyon modeli erkenden netleştirildi.
- **Neyin Geliştirilebileceği:** İletişim sıklığı artırılabilir, fikir seçimi aşamasındaki tartışmalar daha kısa sürede sonuçlandırılabilirdi.
- **Aksiyon Planı:** Bir sonraki sprintte React frontend arayüzü ile asistanın entegrasyonuna daha erken başlanacak.

---

### Sprint 2

**Tarih Aralığı:** [başlangıç] – [bitiş]

**Backlog Düzeni ve Story Seçimleri**
*(Bu bölüm Sprint 2 planlamasında güncellenecektir)*

**Daily Scrum Notları**
[...]

**Sprint Board Güncellemesi**
[...]

**Ürün Durumu**
[...]

**Sprint Review**
[...]

**Sprint Retrospective**
[...]

---

### Sprint 3 (Final)

**Tarih Aralığı:** [başlangıç] – [bitiş]

**Backlog Düzeni ve Story Seçimleri**
*(Bu bölüm Sprint 3 planlamasında güncellenecektir)*

**Daily Scrum Notları**
[...]

**Sprint Board Güncellemesi**
[...]

**Ürün Durumu**
[...]

**Sprint Review**
[...]

**Sprint Retrospective**
[...]

---

## ⚠️ Önemli Kurallar (Hatırlatma)

- Repo **public** olmalı.
- Ürün **sıfırdan geliştirilmeli**; hazır proje kullanmak, satın alma yapmak veya dışarıdan destek almak **diskalifiye sebebidir**.
- Her sprintin ilerlemesi ve kanıtları düzenli olarak bu repoya eklenmelidir (proje yönetimi puanı buna göre verilir).
- Son teslim: **2 Ağustos Pazar 23:59** — repo, video ve form eksiksiz tamamlanmış olmalı.

---

## 📎 Referanslar

- Resmi şablon repo: https://github.com/YapayZekaveTeknolojiAkademisi/BootcampScrumTemplate/tree/main
