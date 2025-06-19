from fastapi import FastAPI
from uvicorn import run

from routes.auth import auth_router
from routes.trips import trip_router
from database import Base, engine, wait_for_db
from models import User, Trip

app = FastAPI()

# Wait for database to be ready
wait_for_db()

# Create Tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(auth_router)
app.include_router(trip_router)

if __name__ == "__main__":
    run(
        app,
        host="0.0.0.0", port=8000
    )

