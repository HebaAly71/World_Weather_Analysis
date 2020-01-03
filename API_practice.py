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
