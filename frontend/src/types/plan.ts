// Backend `app/models/schemas.py` ile aynı şekli paylaşır.

export interface Summary {
  title: string
  region: string
  nights: number
}

export interface Overview {
  procedure: string
  clinicName: string
}

export interface Travel {
  origin: string
  destination: string
  destinationCity: string
  airline: string
  priceGBP: number
}

export interface Accommodation {
  hotelName: string
  nights: number
  priceGBP: number
}

export interface Doctor {
  name: string
  specialty: string
  yearsExperience: number
  rating: number
  boardCertified: boolean
  initials: string
}

export interface DateRange {
  start: string
  end: string
  startISO: string
  endISO: string
}

export interface TripPlan {
  summary: Summary
  overview: Overview
  travel: Travel
  accommodation: Accommodation
  doctor: Doctor
  treatmentCostGBP: number
  dates: DateRange
  disclaimer: string
}

export interface ChatMessage {
  role: 'user' | 'assistant'
  content: string
}

// Arayüzde gösterilen mesaj (opsiyonel zaman damgası ile)
export interface UiMessage {
  role: 'user' | 'assistant'
  content: string
  time?: string
}

export interface ChatResponse {
  reply: string
  plan?: TripPlan | null
}
