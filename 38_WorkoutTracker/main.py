import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv('../.env')

NUTIRION_API_ID = os.getenv('NUTRITION_API_ID')
NUTIRION_API_KEY = os.getenv('NUTRITION_API_KEY')
SHEETY_AUTH_TOKEN = os.getenv('SHEETY_AUTH_TOKEN')
SHEETY_URL = 'https://api.sheety.co/d75e55864dbd2bd91cc468ff28a8f34f/myWorkoutTrackerDemo/sheet1'

header = {
    'x-app-id': NUTIRION_API_ID,
    'x-app-key': NUTIRION_API_KEY
}
# Get exercise data
exercise_text = input('Describe the exercise you did today!: ')

exercise_data = {
    "query": exercise_text,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 28
}

# Retreive calories from Nutrition api
exercise_request = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise' ,data=exercise_data, headers=header)
data = exercise_request.json()['exercises'][0]
print(data)
sheety_header = {
    'Content-Type':'application/json',
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
}
time_now = datetime.now()

# Use Sheety to modify google excel worksheet
exercise_body = {
    'sheet1':{
        'date': f'{time_now.strftime("%Y/%m/%d")}',
        'time': f'{time_now.strftime("%H:%M:%S")}',
        'exercise': f'{data["user_input"]}',
        'duration': f'{data["duration_min"]}',
        'calories': f'{data["nf_calories"]}',
        'id': f'{data["tag_id"]}',
    }
}
exel_request = requests.post(url=SHEETY_URL, json=exercise_body,headers=sheety_header)
print(exel_request.json())