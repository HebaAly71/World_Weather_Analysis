# %%
# Import the requests library.
import requests
# %%
# Import the API key.
from config import weather_api_key

# %%
# Starting URL for Weather Map API Call.
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + weather_api_key
print(url)

# %%
# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
print(city_url)


# %%
url1 = "http://api.openweathermap.org/data/2.5/weather?"
city = "London"
# %%
query_url = url1 + "appid=" + weather_api_key + "&q=" + city
print(query_url)
# %%
weather_response = requests.get(query_url)
weather_json = weather_response.json()
weather_json

# %%
# Make a 'Get' request for the city weather.
city_weather = requests.get(city_url)
city_weather

# %%
# Get the JSON text of the 'Get' request.
city_weather.json()

# %%
# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
city_weather = requests.get(city_url)
if city_weather.status_code == 200:
    print(f"City Weather found.")
else:
    print(f"City weather not found.")

# %%
# Get the JSON data.
boston_data = city_weather.json()

# %%
boston_data['sys']


# %%
boston_data['sys']['country']

# %%
boston_data['coord']['lat']


# %%
lat = boston_data["coord"]["lat"]
lng = boston_data["coord"]["lon"]
max_temp = boston_data["main"]["temp_max"]
humidity = boston_data["main"]["humidity"]
clouds = boston_data["clouds"]["all"]
wind = boston_data["wind"]["speed"]
print(lat, lng, max_temp, humidity, clouds, wind)

# %%
# Import the datetime module from the datetime library.
from datetime import datetime
# Get the date from the JSON file.
date = boston_data["dt"]
# Convert the UTC date to a date format with year, month, day, hours, minutes, and seconds.
datetime.utcfromtimestamp(date)

# %%
# Import the time module.
import time
# Get today's date in seconds.
today = time.time()
today

# %%
