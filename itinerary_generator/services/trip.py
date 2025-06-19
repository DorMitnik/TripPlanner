import os
import requests
from models import Trip

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
API_URL = "https://api.together.xyz/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

def generate_trip(trip: Trip, user_prompt: str):
    prompt = (
        f"You are a travel planner. Create a itinerary for a trip to {trip.destination} "
        f"from {trip.start_date.date()} to {trip.end_date.date()}. "
        f"User instructions: {user_prompt.strip()}.\n\n"
        f"Up to 100 words"
    )

    body = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "You are a helpful travel assistant. Only return JSON."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=HEADERS, json=body)

    if response.status_code != 200:
        raise Exception(f"Together AI API error {response.status_code}: {response.text}")

    return response.json()["choices"][0]["message"]["content"]
