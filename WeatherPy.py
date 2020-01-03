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
