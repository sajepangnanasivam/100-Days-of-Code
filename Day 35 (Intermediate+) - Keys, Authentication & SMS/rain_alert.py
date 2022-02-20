import requests
from twilio.rest import Client

API_KEY ="159e4b55480c4b8dcbaf8336bbff33a2"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# Twilio
account_sid = "AC9e106870630dc9dc22401403cf1d3720"
auth_token = "634149adeb9656c9f11f40d6e22350fc"


# API_URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly&appid={API_KEY}"

weather_params = {
    "lat": 60.035919,
    "lon": 11.125350,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_slice = weather_data["hourly"][:12]
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, remember to bring an umbrella ☂",
        from_='+19126003699',
        to='+4747715752'
    )
    print(message.status)






# print(weather_data)

