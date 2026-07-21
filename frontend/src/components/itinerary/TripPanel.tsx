import type { TripPlan } from '../../types/plan'
import { openBookingLinks } from '../../utils/booking'
import OverviewCard from './OverviewCard'
import TravelCard from './TravelCard'
import AccommodationCard from './AccommodationCard'
import MedicalProfileCard from './MedicalProfileCard'
import CostSummary from './CostSummary'
import Disclaimer from './Disclaimer'

export default function TripPanel({ plan }: { plan: TripPlan | null }) {
  return (
    <aside className="trip">
      <header className="trip-head">
        <div>
          <b>Trip Itinerary</b>
          <small>{plan ? `${plan.summary.title} (${plan.summary.nights} Nights)` : 'Planınız burada belirecek'}</small>
        </div>
        <button className="close" aria-label="Kapat">×</button>
      </header>

      {plan ? (
        <div className="trip-body">
          <OverviewCard overview={plan.overview} nights={plan.summary.nights} />
          <TravelCard travel={plan.travel} />
          <AccommodationCard accommodation={plan.accommodation} />
          <MedicalProfileCard doctor={plan.doctor} />
          <CostSummary plan={plan} />
          <Disclaimer text={plan.disclaimer} />
          <div className="trip-actions">
            <button className="cta" onClick={() => openBookingLinks(plan)}>
              Proceed to Booking
            </button>
            <button className="ghost">⤴ Share</button>
          </div>
        </div>
      ) : (
        <div className="trip-body">
          <div className="trip-empty">
            Sohbete tedavi ve tatil ihtiyacını yaz — kişiselleştirilmiş planın burada oluşacak.
          </div>
        </div>
      )}
    </aside>
  )
}
