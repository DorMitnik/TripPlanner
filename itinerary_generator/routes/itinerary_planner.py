from fastapi import APIRouter, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session
from database import get_db
from fastapi.security import HTTPBearer

from services.auth import decrypt_token
from itinerary_generator.models import Trip, Itinerary
from itinerary_generator.services.trip import generate_trip

router = APIRouter(prefix='/itinerary')
http_bearer = HTTPBearer()


@router.post('/generate-itinerary/{trip_id}')
def generate_itinerary(user_prompt: str, trip_id: int, db: Session = Depends(get_db),
                       credentials: str = Depends(http_bearer)):
    token_data = decrypt_token(credentials.credentials)
    trip = db.query(Trip).filter(Trip.id == trip_id, Trip.user_id == token_data.get("user_id")).first()
    if not trip:
        return Response(status_code=404, content=f"Trip with id: {trip_id} not found")
    trip_suggestion = generate_trip(trip=trip, user_prompt=user_prompt)
    itinerary = Itinerary(user_id=trip.user_id, suggestion=trip_suggestion)
    db.add(itinerary)
    db.commit()
    db.refresh(itinerary)
    return trip_suggestion
