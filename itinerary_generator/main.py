from fastapi import FastAPI
from uvicorn import run
from routes.itinerary_planner import router
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, wait_for_db

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Wait for database to be ready
wait_for_db()

# Create Tables
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(router)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
