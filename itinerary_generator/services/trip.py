import os
import openai
from itinerary_generator.models import Trip

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_trip(trip: Trip, user_prompt: str):
    prompt = (
        f"You are planning a trip to {trip.destination}.\n"
        f"The trip starts on {trip.start_date.date()} and ends on {trip.end_date.date()}.\n"
        f"User instructions: {user_prompt}\n\n"
        f"Create a day-by-day itinerary in JSON format like this:\n"
        f'{{"itinerary": [{{"day_number": 1, "activities": ["Activity 1", "Activity 2"]}}, ...]}}'
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful travel assistant. Always respond in JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content



