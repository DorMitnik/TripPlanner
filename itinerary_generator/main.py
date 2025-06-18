from fastapi import FastAPI
from uvicorn import run
from routes.itinerary_planner import router
from database import Base, engine

app = FastAPI()

# Include router
app.include_router(router)

# Create Tables
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
