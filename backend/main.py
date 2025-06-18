from fastapi import FastAPI
from uvicorn import run

from routes.auth import auth_router
from routes.trips import trip_router
from database import Base, engine
from models import User, Trip
app = FastAPI()

# Routers
app.include_router(auth_router)
app.include_router(trip_router)

# Create Tables
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    run(
        app,
        host="0.0.0.0", port=8000
    )

