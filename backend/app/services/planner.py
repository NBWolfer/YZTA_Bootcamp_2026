"""Kural tabanlı 'AI' planlayıcı (mock mod).

Mesajdan niyet (işlem türü + bölge + bütçe) çıkarır, `matching` ile eşleştirir
ve paneli dolduracak yapılandırılmış `TripPlan` + canned bir yanıt üretir.
Gerçek Gemini bağlanınca (`llm.py`) bu modül aynı şekli üreten fallback olur.
"""
import re
from datetime import date, timedelta
from typing import Optional

from ..models.schemas import (
    Accommodation,
    ChatRequest,
    ChatResponse,
    DateRange,
    Doctor,
    Overview,
    Summary,
    Travel,
    TripPlan,
)
from . import matching

DISCLAIMER = (
    "HealRoute AI tıbbi tavsiye vermez; yalnızca seyahat planlaması ve klinik "
    "listeleme hizmeti sunar. Nihai tedavi kararı için lisanslı bir hekime danışın."
)

PROCEDURE_LABELS = {
    "dental-implant": "Dental implants",
    "teeth-whitening": "Teeth whitening",
    "botox": "Botox",
    "dermal-filler": "Dermal fillers",
}

DENTAL = {"dental-implant", "teeth-whitening"}
DEFAULT_NIGHTS = 5


def _clean(text: str) -> str:
    # Türkçe 'İ'.lower() birleşik nokta (U+0307) üretir; kaldırıp normalize ediyoruz.
    return text.lower().replace("̇", "")


def detect_procedure(text: str) -> str:
    t = _clean(text)
    if "implant" in t:
        return "dental-implant"
    if "whiten" in t or "beyaz" in t:
        return "teeth-whitening"
    if "botox" in t or "botoks" in t:
        return "botox"
    if "filler" in t or "dolgu" in t:
        return "dermal-filler"
    if any(k in t for k in ("dental", "teeth", "diş", "dis", "tooth")):
        return "dental-implant"
    if "aesthetic" in t or "estetik" in t:
        return "botox"
    return "dental-implant"  # varsayılan (mockup senaryosu)


def detect_location(text: str):
    t = _clean(text)
    if "fethiye" in t:
        return "Muğla", "Fethiye"
    if "bodrum" in t:
        return "Muğla", "Bodrum"
    if "muğla" in t or "mugla" in t:
        return "Muğla", None
    if "istanbul" in t or "ıstanbul" in t:
        return "İstanbul", "İstanbul"
    return "Muğla", "Bodrum"  # varsayılan (mockup senaryosu)


def detect_budget(text: str) -> Optional[int]:
    m = re.search(r"[£$€₺]?\s?(\d{3,6})", text.replace(",", ""))
    return int(m.group(1)) if m else None


def _journey_label(procedure: str) -> str:
    return "Dental" if procedure in DENTAL else "Aesthetic"


def build_plan_and_reply(req: ChatRequest) -> ChatResponse:
    procedure = detect_procedure(req.message)
    region, city = detect_location(req.message)
    budget = detect_budget(req.message)

    result = matching.match(procedure, region, city, budget)
    if result is None:
        return ChatResponse(
            reply=(
                "Şu an bu işlem/bölge kombinasyonu için pilot kliniğimiz yok. "
                "Bodrum veya İstanbul'da diş (implant/beyazlatma) ya da estetik "
                "(botoks/dolgu) işlemleri için yardımcı olabilirim."
            ),
            plan=None,
        )

    clinic, doctor, hotel, flight = result
    nights = DEFAULT_NIGHTS
    city_name = clinic["city"]
    journey = _journey_label(procedure)
    proc_label = PROCEDURE_LABELS[procedure]

    start = date.today() + timedelta(days=30)
    end = start + timedelta(days=nights)
    date_range = DateRange(
        start=start.strftime("%b %d"),
        end=end.strftime("%b %d, %Y"),
        startISO=start.isoformat(),
        endISO=end.isoformat(),
    )

    plan = TripPlan(
        summary=Summary(title=f"{city_name} {journey} Journey", region=region, nights=nights),
        overview=Overview(procedure=proc_label, clinicName=clinic["name"]),
        travel=Travel(
            origin=flight["origin"],
            destination=flight["destination"],
            destinationCity=flight["destinationCity"],
            airline=flight["airline"],
            priceGBP=flight["priceGBP"],
        ),
        accommodation=Accommodation(
            hotelName=hotel["name"],
            nights=nights,
            priceGBP=hotel["nightlyGBP"] * nights,
        ),
        doctor=Doctor(**doctor),
        treatmentCostGBP=clinic["priceGBP"][procedure],
        dates=date_range,
        disclaimer=DISCLAIMER,
    )

    reply = (
        f"Absolutely! I can help you plan your {city_name} {journey.lower()} journey. "
        f"Based on your preferences, I've curated a {city_name} package with "
        f"{clinic['name']} (rated {clinic['rating']}/5), flights, and accommodation. "
        f"Here's a summary on the right!"
    )
    return ChatResponse(reply=reply, plan=plan)
