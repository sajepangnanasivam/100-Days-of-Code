# -------- Imports -------- #
import requests
from datetime import datetime

# -------- Creating Constants for the project -------- #
APP_ID = "c297dee9"
API_KEY = "52cd4f1a484e08793dcdf4fd39dbd25e"
GENDER = "male"
WEIGHT_KG = 90.5
HEIGHT_CM = 190.1
AGE = 24

# API Authentication
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/eaefc4362b95f968e59e3a14bb4e3569/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)