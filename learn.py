# ee71778faf28390f6efd726be25ead22

api_key = "ee71778faf28390f6efd726be25ead22"
# http://api.openweathermap.org/data/2.5/weather?q=Nairobi&appid=2104b60721e212ce450ad3a10f14a8a4

# http://api.openweathermap.org/data/2.5/weather?q=Nakuru&appid=2104b60721e212ce450ad3a10f14a8a4

# http://api.openweathermap.org/data/2.5/weather?q=Kutus&appid=2104b60721e212ce450ad3a10f14a8a4

# kutus latitude = -0.567030 longitude = 37.325291

# kutus weather forecasts
import requests

# raw_data = requests.get(url='https://api.openweathermap.org/data/2.5/onecall?lat=-0.567030&lon=37.325291&&appid=2104b60721e212ce450ad3a10f14a8a4')

# data = raw_data.json()
# print(data)


# instructor's solution
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    'lat': -0.567030,
    'lon' : 37.325291,
    'appid': '2104b60721e212ce450ad3a10f14a8a4',
    'exclude': 'current,minutely,daily'
}
response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data['hourly'][0]['weather'][0])
weather_slice = weather_data['hourly'][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        print("Bring an Umbrella")
    elif int(condition_code) > 700:
        print("No need for an Umbrella today.")