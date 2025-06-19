from fastapi import FastAPI
from uvicorn import run
from routes.itinerary_planner import router
from database import Base, engine, wait_for_db

app = FastAPI()

# Wait for database to be ready
wait_for_db()

# Create Tables
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(router)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
