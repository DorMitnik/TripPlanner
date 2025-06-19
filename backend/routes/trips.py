from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from database import get_db
from models import Trip
from schemas import TripCreate, TokenData
from services.auth import decrypt_token
from starlette.responses import Response

trip_router = APIRouter()
http_bearer = HTTPBearer()


@trip_router.post("/trips")
def create_trip(trip: TripCreate, db: Session = Depends(get_db), credentials: str = Depends(http_bearer)):
    token_data = decrypt_token(credentials.credentials)
    new_trip = Trip(**trip.dict(), user_id=token_data.get("user_id"))
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)
    return new_trip


@trip_router.get("/trips")
def list_trips(db: Session = Depends(get_db), credentials: str = Depends(http_bearer)):
    token_data = decrypt_token(credentials.credentials)
    return db.query(Trip).filter(Trip.user_id == token_data["user_id"] ).all()


@trip_router.delete("/trips")
def delete_trip(trip_id: int, db: Session = Depends(get_db), credentials: str = Depends(http_bearer)):
    token_data = decrypt_token(credentials.credentials)
    trip = db.query(Trip).filter(Trip.id == trip_id and Trip.user_id == token_data.get("user_id")).first()
    if not trip:
        return Response(status_code=404, content=f"No trip found with id: {trip_id}")
    db.delete(trip)
    db.commit()
    return Response(status_code=200, content=f"trip with id: {trip_id} deleted")
