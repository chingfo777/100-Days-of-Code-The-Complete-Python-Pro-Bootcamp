import requests
from twilio.rest import Client

OWM_Endpoint= "https://api.openweathermap.org/data/2.5/forecast"
api_key= ""
account_sid = ""
auth_token = ""
weather_params={
    "lat": 23.445110,
    "lon": 88.311493,
    "appid": api_key,
    "cnt":4,
}
response = requests.get(OWM_Endpoint,weather_params)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = (client.messages
               .create(
        body="Hare Krishna! It's going to rain today.\n Remember to bring an ☔",
        from_='+18569256960',
        to=''
    ))
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = (client.messages
    .create(
        body="Hare Krishna! Good Morning! Its a Sunnyday!🌄🌅😎",
        from_='+18569256960',
        to=''
    ))
    print(message.status)
