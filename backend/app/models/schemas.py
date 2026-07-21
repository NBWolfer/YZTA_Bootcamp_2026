"""Pydantic şemaları — frontend `types/plan.ts` ile aynı şekli paylaşır."""
from typing import List, Optional

from pydantic import BaseModel


class Summary(BaseModel):
    title: str
    region: str
    nights: int


class Overview(BaseModel):
    procedure: str
    clinicName: str


class Travel(BaseModel):
    origin: str
    destination: str
    destinationCity: str
    airline: str
    priceGBP: int


class Accommodation(BaseModel):
    hotelName: str
    nights: int
    priceGBP: int


class Doctor(BaseModel):
    name: str
    specialty: str
    yearsExperience: int
    rating: float
    boardCertified: bool
    initials: str


class DateRange(BaseModel):
    start: str
    end: str
    startISO: str
    endISO: str


class TripPlan(BaseModel):
    summary: Summary
    overview: Overview
    travel: Travel
    accommodation: Accommodation
    doctor: Doctor
    treatmentCostGBP: int
    dates: DateRange
    disclaimer: str


class ChatMessage(BaseModel):
    role: str  # "user" | "assistant"
    content: str


class ChatRequest(BaseModel):
    message: str
    history: List[ChatMessage] = []


class ChatResponse(BaseModel):
    reply: str
    plan: Optional[TripPlan] = None
