# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Import the random module.
import random
# Import the dependencies.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# %%
# Create a set of random latitude and longitude combinations.
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)
lat_lngs 


# %%
# Add the latitudes and longitudes to a list.
coordinates = list(lat_lngs)


# %%
from citipy import citipy


# %%
# Create a list for holding the cities.
cities = []
# Identify the nearest city for each latitude and longitude combination.
for coordinate in coordinates:
    city = citipy.nearest_city(coordinate[0], coordinate[1]).city_name
    
    # If the city is unique, then we will add it to the cities list.
    if city not in cities:
        cities.append(city)
# Print the city count to confirm sufficient count.
len(cities)


# %%
# Import the requests library.
import requests
from datetime import datetime


# %%
# Import the API key.
from config import weather_api_key


# %%
# Starting URL for Weather Map API Call.
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + weather_api_key

# %%
city_weather = requests.get(city_url).json()
city_weather
# %%
# Create an empty list to hold the weather data.
city_data = []
# Print the beginning of the logging.
print("Beginning Data Retrieval     ")
print("-----------------------------")

# Create counters.
record_count = 1
set_count = 1
# Loop through all the cities in the list.
for i, city in enumerate(cities):

    # Group cities in sets of 50 for logging purposes.
    if (i % 50 == 0 and i >= 50):
        set_count += 1
        record_count = 1
    # Create endpoint URL with each city.
    city_url = url + "&q=" + city

    # Log the URL, record, and set numbers and the city.
    print(f"Processing Record {record_count} of Set {set_count} | {city}")
    # Add 1 to the record count.
    record_count += 1
    # Run an API request for each of the cities.
    try:
        # Parse the JSON and retrieve data.
        city_weather = requests.get(city_url).json()
        # Parse out the needed data.
        city_lat = city_weather["coord"]["lat"]
        city_lng = city_weather["coord"]["lon"]
        city_max_temp = city_weather["main"]["temp_max"]
        city_humidity = city_weather["main"]["humidity"]
        city_clouds = city_weather["clouds"]["all"]
        city_wind = city_weather["wind"]["speed"]
        city_country = city_weather["sys"]["country"]
        try:
            city_rain = city_weather["rain"]["3h"]
        except:
            city_rain = 0
            print('No rain')
        try:
            city_snow = city_weather["snow"]["3h"]
        except:
            city_snow = 0
            print('No snow')
        city_descp = city_weather['weather'][0]['description']
        #city_rain = city_weather["rain"]["3h"]
        #city_snow = city_weather["snow"]["3h"]
        # Convert the date to ISO standard.
        city_date = datetime.utcfromtimestamp(city_weather["dt"]).strftime('%Y-%m-%d %H:%M:%S')
        # Append the city information into city_data list.
        city_data.append({"City": city.title(),
                          "Lat": city_lat,
                          "Lng": city_lng,
                          "Max Temp": city_max_temp,
                          "Humidity": city_humidity,
                          "Cloudiness": city_clouds,
                          "Wind Speed": city_wind,
                          "Country": city_country,
                          "Date": city_date, 
                          "Rain inches (last 3 hours)": city_rain, 
                          "Snow inches (last 3 hours)": city_snow, 
                          "Current Descrption": city_descp})

# If an error is experienced, skip the city.
    except:     
        print("City not found. Skipping...")
    pass

# Indicate that Data Loading is complete.
print("-----------------------------")
print("Data Retrieval Complete      ")
print("-----------------------------")


# %%
len(city_data)


# %%
# Convert the array of dictionaries to a Pandas DataFrame.
city_data_ch_df = pd.DataFrame(city_data)
city_data_ch_df.head(10)


# %%
new_column_order = ["City", "Country", "Date", "Lat", "Lng", "Max Temp", "Humidity", "Cloudiness", "Wind Speed", 'Current Descrption', "Rain inches (last 3 hours)",'Snow inches (last 3 hours)']
city_data_ch_df=city_data_ch_df[new_column_order]


# %%
city_data_ch_df.head(10)


# %%
# Create the output file (CSV).
output_data_file = "weather_data/weatherpy_challenge.csv"
# Export the City_Data into a CSV.
city_data_ch_df.to_csv(output_data_file, index_label="City_ID")
# %%

# 

