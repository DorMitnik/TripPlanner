from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hashed = Column(String)
    email = Column(String, unique=True, index=True)

    trips = relationship("Trip", back_populates="user")

class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    destination = Column(String)
    start_date = Column(DateTime(timezone=True))
    end_date = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="trips")
