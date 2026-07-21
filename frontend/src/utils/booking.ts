import type { TripPlan } from '../types/plan'

// checkin/checkout tarihlerini YYMMDD'ye çevirir (Skyscanner URL segmenti için).
function toSkyscannerDate(iso: string): string {
  return iso.replace(/-/g, '').slice(2)
}

export function buildBookingUrl(plan: TripPlan): string {
  // Booking.com'un `ss` parametresi serbest metin değil, kendi autocomplete
  // veritabanına karşı eşleşiyor: otel adı eklemek veya Türkçe aksan (İ, ğ)
  // kullanmak eşleşmeyi bozup kullanıcıyı ana sayfaya düşürüyor. Yalnızca
  // düz şehir adı (ör. "Bodrum", "Istanbul") güvenilir şekilde çalışıyor.
  const params = new URLSearchParams({
    ss: plan.travel.destinationCity,
    checkin: plan.dates.startISO,
    checkout: plan.dates.endISO,
    group_adults: '1',
    no_rooms: '1',
  })
  return `https://www.booking.com/searchresults.html?${params.toString()}`
}

export function buildSkyscannerUrl(plan: TripPlan): string {
  const origin = plan.travel.origin.toLowerCase()
  const destination = plan.travel.destination.toLowerCase()
  const outbound = toSkyscannerDate(plan.dates.startISO)
  const inbound = toSkyscannerDate(plan.dates.endISO)
  return `https://www.skyscanner.net/transport/flights/${origin}/${destination}/${outbound}/${inbound}/`
}

export function openBookingLinks(plan: TripPlan): void {
  window.open(buildSkyscannerUrl(plan), '_blank', 'noopener,noreferrer')
  window.open(buildBookingUrl(plan), '_blank', 'noopener,noreferrer')
}
