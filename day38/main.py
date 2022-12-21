import requests
from datetime import datetime

GENDER = "MALE"
WEIGHT_KG = "62"
HEIGHT = "175" #entered random height in cm
AGE = "34"
APP_ID ="your app_id"
API_KEY = "your app key"
sheet_token="your sheet token"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    # i ran 3 miles and walked 3km
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()

today = datetime.now().strftime("%Y/%m/%d")
time = datetime.now().strftime("%H:%M")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
 
headers = {"Authorization": f"Bearer {sheet_token}"}
SHEETY_API_URL = "https://api.sheety.co"

sheet_response = requests.post(url=SHEETY_API_URL, json=sheet_inputs, headers=header)
print(sheet_response.text)
 