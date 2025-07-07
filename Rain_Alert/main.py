import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="Rain_Alert/main.env")
import requests

from twilio.rest import Client
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

API_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY =  os.getenv("API_KEY")
MY_LATITUDE = os.getenv("MY_LATITUDE")
MY_LONGITUDE = os.getenv("MY_LONGITUDE")

if not API_KEY:
    raise Exception("API_KEY not found.")

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 8
}

response = requests.get(url= API_URL, params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700: 
        will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    messaging_service_sid=os.getenv("messaging_service_sid"),
    body= "It's going to rain today. Remember to bring an ☂️",
    to=os.getenv("to")
    )
    print(message.status)