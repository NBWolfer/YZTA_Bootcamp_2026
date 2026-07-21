# Deploy Rehberi (US-10)

Kod tarafı deploy'a hazır: backend `Dockerfile` ve `ALLOWED_ORIGINS` env değişkenini,
frontend `VITE_API_BASE_URL` env değişkenini destekliyor. Kalan adımlar hesap
girişi gerektirdiği için (Claude hesap oluşturamaz/parola giremez) burada manuel
olarak izlenecek.

## 1. Backend — Render (ücretsiz plan)

1. https://render.com adresinde GitHub hesabınla giriş yap.
2. **New +** → **Web Service** → bu repoyu seç.
3. Ayarlar:
   - **Root Directory:** `backend`
   - **Environment:** Docker (Dockerfile otomatik algılanır)
   - **Instance Type:** Free
4. **Environment Variables** ekle:
   - `USE_GEMINI=false` (mock modda kalmak için; gerçek Gemini için Erkin'in US-05'i bittiğinde `true` + `GEMINI_API_KEY`)
   - `ALLOWED_ORIGINS` → frontend deploy edildikten sonra 3. adımda eklenecek
5. Deploy'u başlat, bitince verilen URL'i not al (ör. `https://healroute-api.onrender.com`).
6. `https://<backend-url>/health` adresini ziyaret ederek `{"status":"ok","mode":"mock"}` döndüğünü doğrula.

## 2. Frontend — Vercel (ücretsiz plan)

1. https://vercel.com adresinde GitHub hesabınla giriş yap.
2. **Add New** → **Project** → bu repoyu seç.
3. Ayarlar:
   - **Root Directory:** `frontend`
   - **Framework Preset:** Vite (otomatik algılanır)
4. **Environment Variables** ekle:
   - `VITE_API_BASE_URL=https://healroute-api.onrender.com` (1. adımdaki backend URL'i)
5. Deploy et, verilen URL'i not al (ör. `https://healroute-ai.vercel.app`).

## 3. CORS'u kapat

Render'a dön → backend servisinin **Environment** sekmesi →
`ALLOWED_ORIGINS=https://healroute-ai.vercel.app` (2. adımdaki frontend URL'i) ekle
→ servisi yeniden deploy et (redeploy).

## 4. Uçtan uca doğrula

Frontend URL'ini tarayıcıda aç, "Bodrumda diş implantı yaptırmak istiyorum" yaz,
plan panelinin dolduğunu ve "Proceed to Booking" butonunun Booking.com/Skyscanner'ı
açtığını doğrula.

## 5. README'yi güncelle

`README.md` içindeki `🔗 [Canlı Demo Linki](#)` satırını gerçek frontend URL'i ile değiştir.
