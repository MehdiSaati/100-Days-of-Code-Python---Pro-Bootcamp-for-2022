import requests
import os
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "d4e3395720ae372db7310ff3cfd46ca9"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


weather_params = {
    "lat": 34.797032,
    "lon": 48.514681,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # print("Bring an Umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella.",
                        from_='+15017122661',
                        to='+15558675310'
                    )

    print(message.status)
 
