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

🔗 [Trello Backlog Board](https://trello.com/invite/b/6a3fbc8a64ba7c4eed355b9c/ATTI3a02fc2e96b300a202e996bae02d7784441CC8B4/agile-sprint-board-template)

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
- Proje takibi için Trello panosu aktif olarak kullanılmaktadır. İlgili görevlerin durumları (Done, In Progress, Sprint Backlog, Backlog) düzenli olarak güncellenmektedir.

![Sprint 1 Trello Board](assets/sprint_board.png)

**Ürün Durumu**
- Gemini API ile entegre, terminal üzerinden çalışan ilk prototip (PoC) tamamlandı. Pilot bölge ve tedavi verileri mock JSON formatında sisteme bağlandı.

![HealRoute AI Sprint 1 Prototip](assets/product_sprint1.png)

**Sprint Review**
- **Tamamlanan İşler:** Fikir seçimi yapıldı, PRD.md hazırlandı, Gemini API entegrasyonu sağlandı ve ilk mock veri kümesi oluşturuldu. Sprint hedeflerinin %100'ü başarıyla tamamlandı.

**Sprint Retrospective**
- **Neyin İyi Gittiği:** Takım içi karar alma süreci hızlı ve yapıcı ilerledi. Teknik altyapı ve AI entegrasyon modeli erkenden netleştirildi.
- **Neyin Geliştirilebileceği:** İletişim sıklığı artırılabilir, fikir seçimi aşamasındaki tartışmalar daha kısa sürede sonuçlandırılabilirdi.
- **Aksiyon Planı:** Bir sonraki sprintte React frontend arayüzü ile asistanın entegrasyonuna daha erken başlanacak.

---

### Sprint 2

**Tarih Aralığı:** 6 Temmuz 2026 – 19 Temmuz 2026

**Sprint Hedefi**
Sprint 1'de terminal üzerinde çalışan Gemini PoC'yi, `assets/product_sprint1.png` tasarımına uygun **React tabanlı web arayüzüne** taşımak; sohbet panelini ve "Trip Itinerary" (seyahat + tedavi planı) panelini yapay zeka çıktısıyla besleyen uçtan uca bir demo çıkarmak.

**Backlog Düzeni ve Story Seçimleri**
- [x] **US-01 – Frontend iskeleti:** React (Vite + TypeScript) kurulumu, dark tema tasarım sistemi (renk/tipografi) ve üç kolonlu ana layout (rail + sohbet + plan paneli). `frontend/src/theme`, `Rail.tsx`, `ChatPanel`, `TripPanel` ile tamamlandı; `npm run build` hatasız geçiyor.
- [x] **US-02 – Sohbet arayüzü:** Mesaj listesi, kullanıcı/asistan balonları, konu başlığı çipi ve mesaj gönderme alanı. `ChatPanel`, `MessageBubble`, `TopicChip`, `Composer` bileşenleriyle tamamlandı.
- [x] **US-03 – Trip Itinerary paneli:** Itinerary Overview, Travel, Accommodation, Medical Profile, tedavi maliyeti ve tarih kartlarının bileşen olarak kurulması. `TripPanel` altında ilgili tüm kart bileşenleri mevcut.
- [x] **US-04 – Backend API katmanı:** Terminal PoC'deki planlama mantığının REST endpoint'ine taşınması — FastAPI ile `POST /api/chat` ve `GET /health` uçları çalışır durumda (canlı test edildi). Not: Ayrı bir `/plan` endpoint'i açılmadı; plan verisi `/api/chat` yanıtına gömülü olarak dönüyor.
- [ ] **US-05 – Yapılandırılmış AI çıktısı:** *(Kısmi)* `TripPlan` JSON şeması (`backend/app/models/schemas.py`) tanımlandı ve kural tabanlı mock planlayıcı (`services/planner.py`) bu şemaya uygun veriyi güvenilir şekilde üretiyor. Ancak gerçek Gemini entegrasyonu henüz yok — `services/llm.py` içinde `_generate_with_gemini` bilinçli olarak `NotImplementedError` fırlatıp mock'a düşüyor. **Sprint 3'e taşınıyor.**
- [x] **US-06 – Klinik eşleştirme motoru v1:** Mock veri üzerinde işlem türü + bölge/şehir + bütçeye göre klinik önerme mantığı `services/matching.py` içinde tamamlandı ve test edildi.
- [x] **US-07 – Mock veri genişletme:** Muğla (Bodrum, Fethiye) ve İstanbul için 9 klinik, 9 doktor, 5 otel, 4 uçuş kaydından oluşan mock veri seti `backend/app/data/*.json` altında oluşturuldu.
- [ ] **US-08 – Yasal uyarı & rezervasyon iskeleti:** *(Kısmi)* Disclaimer bileşeni (`Disclaimer.tsx`) tamamlandı ve plan panelinde gösteriliyor. Ancak "Proceed to Booking" butonu şu an işlevsiz bir `<button>` — Booking.com/Skyscanner'a giden gerçek bir deep-link (URL/href) henüz bağlanmadı. **Sprint 3'e taşınıyor.**
- [x] **US-09 – Uçtan uca entegrasyon:** Frontend ↔ Backend bağlantısı (Vite dev proxy → FastAPI) çalışıyor; "Bodrum diş implantı" senaryosu uçtan uca test edildi ve plan paneli doğru JSON ile doluyor.

> Sonuç: 9 story'den 7'si tamamlandı (US-01, 02, 03, 04, 06, 07, 09). US-05 (gerçek Gemini entegrasyonu) ve US-08 (booking deep-link) kısmi kalıp Sprint 3'e taşındı.

**Daily Scrum Notları**
Git geçmişi bu sprint boyunca günlük commit içermiyor; ekip çalışmayı çoğunlukla yerelde ilerletip sprint sonunda tek seferde entegre etti. Kayıtlı iki dönüm noktası:
- **7 Temmuz Salı:** Mentor geri bildirimleri README'ye işlendi (`8c00bf1 docs: mentor feedback`).
- **18 Temmuz Cumartesi:** React frontend (Vite + TS) ve FastAPI backend'i aynı gün içinde tamamlanıp tek commit'te birleştirildi (`9fde46e feat: integrate React frontend and FastAPI backend for Sprint 2`), ardından `.gitignore` eklenip `node_modules` takipten çıkarıldı (`b06c49c`) ve `main`'e PR #1 ile merge edildi (`5dacf42`).
- **Not (Retrospective'e taşındı):** `backend/.venv` bu commit'te yanlışlıkla ~2500 dosyayla birlikte git'e eklenmiş; sprint wrap-up'ında takipten çıkarıldı.

**Sprint Board Güncellemesi**
Trello panosundaki Sprint 2 kartları bu README'deki tamamlanma durumuyla eşleşecek şekilde güncellenmiştir: US-01, US-02, US-03, US-04, US-06, US-07, US-09 -> **Sprint 2 Done** listesine taşınmış; US-05, US-08 ise **Sprint 3 Backlog** listesine aktarılmıştır.

![Sprint 2 Trello Board](assets/sprint_board_2.png)

**Ürün Durumu**
Sprint 1'deki terminal PoC, dark temalı üç kolonlu bir React arayüzüne (Rail + Sohbet + Trip Itinerary paneli) taşındı ve FastAPI backend'ine bağlandı. Mock modda (`USE_GEMINI=false`, varsayılan) `/api/chat` uç noktası test edildi: "Bodrumda diş implantı yaptırmak istiyorum, 3000 GBP bütçem var" mesajı gönderildiğinde klinik, doktor, otel, uçuş ve tedavi maliyetini içeren tam bir `TripPlan` JSON'u dönüyor ve arayüzde plan paneline doğru şekilde yansıyor. Gerçek Gemini API bağlantısı henüz aktif değil (mock planlayıcıya güvenli fallback var); bu Sprint 3'ün kapsamında.

**Sprint Review**
- **Tamamlanan İşler:** 9 story'den 7'si (US-01, 02, 03, 04, 06, 07, 09) tamamlandı ve kodda doğrulandı — frontend derleniyor (`npm run build`), backend canlı olarak test edildi.
- **Tamamlanmayan/Kısmi İşler:** US-05 (gerçek Gemini entegrasyonu, şu an mock) ve US-08 (booking deep-link'i, şu an disclaimer var ama rezervasyon linki yok) Sprint 3'e devrediliyor.
- **Genel Değerlendirme:** Sprint hedefinin özü (terminal PoC → çalışan React+FastAPI web demosu) başarıyla karşılandı; yapay zeka tarafındaki son mil (gerçek LLM çağrısı) ve rezervasyon entegrasyonu bilinçli olarak ertelendi.

**Sprint Retrospective**
- **Neyin İyi Gittiği:** Frontend, backend ve mock veri katmanları birbirinden bağımsız geliştirilebilecek şekilde net ayrıştırıldı ve tek entegrasyon adımında sorunsuz birleşti; uçtan uca demo senaryosu ilk denemede çalıştı.
- **Neyin Geliştirilebileceği:** Sprint boyunca commit sıklığı çok düşüktü (pratikte tek büyük iş commit'i) — bu hem ilerlemenin repo üzerinden izlenmesini zorlaştırdı hem de `backend/.venv`'in yanlışlıkla commit edilmesi gibi bir hataya yol açtı. Ayrıca Sprint hedefinde "US-08/US-09 Sprint 3'e taşınabilir" öngörülmüştü; gerçekte US-09 tamamlandı ama US-05 kısmi kaldı — kapsam tahmini gözden geçirilmeli.
- **Aksiyon Planı:** Sprint 3'te (1) daha sık ve küçük commit'ler atılacak, (2) `.venv`/`node_modules` gibi üretilmiş klasörlerin ilk kurulumda `.gitignore`'a eklenip hiç commit edilmemesi için commit öncesi `git status` kontrolü alışkanlık haline getirilecek, (3) gerçek Gemini entegrasyonu (US-05) ve Booking.com/Skyscanner deep-link'i (US-08) önceliklendirilecek.

---

### Sprint 3 (Final)

**Tarih Aralığı:** 20 Temmuz 2026 – 2 Ağustos 2026 (kesin teslim: 2 Ağustos Pazar 23:59)

**Sprint Hedefi**
Sprint 2'den kalan iki story'yi kapatmak, ürünü canlıya almak ve teslim için gereken tüm materyalleri (video, final dökümantasyon) tamamlamak.

**Backlog Düzeni ve Story Seçimleri**

| Story | Açıklama | Sahip |
|---|---|---|
| [ ] **US-05 (devir)** – Gerçek Gemini entegrasyonu | `backend/app/services/llm.py` içindeki `_generate_with_gemini` fonksiyonunun `google-generativeai` ile gerçek çağrı yapacak şekilde tamamlanması; TripPlan JSON'unun response-schema ile doğrudan LLM'den üretilmesi (mock planlayıcı fallback olarak kalır). | **Erkin** |
| [ ] **US-08 (devir)** – Booking.com & Skyscanner deep-link | `TripPanel`'daki "Proceed to Booking" butonunun, plandaki tarih/lokasyon/otel bilgilerinden gerçek Booking.com ve Skyscanner sorgu URL'lerini üretip yeni sekmede açacak şekilde bağlanması. | **Kerem** |
| [ ] **US-10** – Canlı demo deploy | Backend (FastAPI) ve frontend'in (Vite build) bir hosting ortamına deploy edilmesi; README'deki "Canlı Demo Linki" placeholder'ının gerçek URL ile güncellenmesi. | **Kerem** |
| [ ] **US-11** – Hata yönetimi & UX cilası | API hata durumlarında kullanıcıya daha net geri bildirim, loading/empty state iyileştirmeleri, temel mobil/responsive düzenlemeler. | **Erkin** |
| [ ] **US-12** – Sunum videosu | Uçtan uca demo senaryosunun (ör. "Bodrum'da diş implantı") video kaydının alınıp YouTube'a yüklenmesi; README'deki video linkinin güncellenmesi. | **Kerem** |
| [ ] **US-13** – Final QA & teslim kontrol listesi | README/PRD tutarlılık kontrolü, "Önemli Kurallar" bölümündeki teslim şartlarının (public repo, video, form) sağlandığının doğrulanması, son uçtan uca regresyon testi. | **Erkin** |

> Not: US-05 ve US-08, Sprint 2'de kısmi kaldığı için buraya devredildi; sahiplik ataması ekip kapasitesi netleşince güncellenebilir.

**Daily Scrum Notları**
_(Sprint boyunca günlük olarak doldurulacaktır.)_

**Sprint Board Güncellemesi**
_(Sprint 3 Trello görünümü sprint sonunda eklenecektir.)_

**Ürün Durumu**
_(Sprint sonunda: canlı demo linki + video ile güncellenecektir.)_

**Sprint Review**
_(Sprint sonunda doldurulacaktır.)_

**Sprint Retrospective**
_(Sprint sonunda doldurulacaktır.)_

---

## ⚠️ Önemli Kurallar (Hatırlatma)

- Repo **public** olmalı.
- Ürün **sıfırdan geliştirilmeli**; hazır proje kullanmak, satın alma yapmak veya dışarıdan destek almak **diskalifiye sebebidir**.
- Her sprintin ilerlemesi ve kanıtları düzenli olarak bu repoya eklenmelidir (proje yönetimi puanı buna göre verilir).
- Son teslim: **2 Ağustos Pazar 23:59** — repo, video ve form eksiksiz tamamlanmış olmalı.

---

## 📎 Referanslar

- Resmi şablon repo: https://github.com/YapayZekaveTeknolojiAkademisi/BootcampScrumTemplate/tree/main
