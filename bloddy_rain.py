import requests
import smtplib

OPW_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "4b61ebe8220dd78c2809cb28df7f4f9e"
parameters = {
    "lat" : 12.971599,
    "lon" : 77.594566,
    "appid" : API_KEY,
    "cnt" : 4
}

MY_EMAIL = "aryapasupulate@gmail.com"
PASS = "yzfajjgoszrcfjuy"

response = requests.get(url=OPW_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, PASS)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg="Subject:Weather Alert....!\n\nThere are chances of rain."
                            "Please carry an Umbrella.")
