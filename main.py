import requests
from datetime import datetime
import os
os.environ


USERNAME = "mariayoana.marinova"
PASSWORD = "Ni$iki.ramen"
app_id = "8fd37541"
app_key = "fe04fdd714031385e08fe43b2ca60a61"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["https://api.sheety.co/b411d0b1ef11bf644de2ae20d8ea798e/workoutTracking/workouts"]


GENDER = "female"
WEIGHT_KG = 62
HEIGHT_SM = 176
AGE = 27
TODAY = datetime.today().strftime("%d/%m/%Y")
TIME = datetime.now().strftime("%X")


exercise_input = input("What kind of work out did you do?: ")

header = {
    "x-app-id": app_id,
    "x-app-key": app_key,
}

header_sheety = {
"Authorization": "Basic bWFyaWF5b2FuYS5tYXJpbm92YTpOaSRpa2kucmFtZW4="

}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_SM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
result = response.json()


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": TODAY,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    print(result)
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=header_sheety)

    print(sheet_response.text)
#Basic Authenticaion

print(os.environ)

