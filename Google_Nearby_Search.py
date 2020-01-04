# %%
# Dependencies and Setup
import requests
import gmaps
# %%

# Import API key
gog_key="AIzaSyBEQEus6VRSAPWyP8vTzczYXwbrG0WG6YU"
# %%
# Set the parameters to search for a hotel in Paris.
params = {
    "radius": 5000,
    "types": "lodging",
    "key": gog_key,
    "location": "48.8566, 2.3522"}
# Use base URL to search for hotels in Paris.
base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
# Make request and get the JSON data from the search.
hotels = requests.get(base_url, params=params).json()

# %%
len(hotels["results"])

# %%
