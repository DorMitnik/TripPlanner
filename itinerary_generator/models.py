from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from database import Base

class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    destination = Column(String)
    start_date = Column(DateTime(timezone=True))
    end_date = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# Only define Itinerary model — no need for relationship if not used
class Itinerary(Base):
    __tablename__ = 'itinerary'
    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, unique=True)
    suggestion = Column(JSONB, nullable=True)
