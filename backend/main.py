from fastapi import FastAPI
from uvicorn import run

from routes.auth import auth_router
from routes.trips import trip_router
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, wait_for_db
from models import User, Trip

app = FastAPI()

# Wait for database to be ready
wait_for_db()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

