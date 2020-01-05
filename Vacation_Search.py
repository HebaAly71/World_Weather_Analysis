# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Import the dependencies.
import pandas as pd
import gmaps
import requests


# %%
# Import the API key.
from config import gog_key


# %%
# Store the CSV you saved created in part one into a DataFrame.
city_data_df = pd.read_csv("weather_data/weatherpy_challenge.csv")
city_data_df.head()


# %%
# Configure gmaps to use your Google API key.
gmaps.configure(api_key=gog_key)


# %%
# Ask the customer to add a minimum and maximum temperature value.
min_temp = float(input("What is the minimum temperature you would like for your trip? "))
max_temp = float(input("What is the maximum temperature you would like for your trip? "))
rain_ans = str(input("Do you want it to be raining? (yes/no) "))
snow_ans = str(input("Do you want it to be snowing? (yes/no) "))


# %%
# Filter the dataset to find the cities that fit the criteria.
if rain_ans == 'yes' and snow_ans == 'yes':
    preferred_cities_df = city_data_df.loc[(city_data_df["Max Temp"] <= max_temp) & (city_data_df["Max Temp"] >= min_temp)& (city_data_df['Rain inches (last 3 hours)'] > 0 ) & (city_data_df['Snow inches (last 3 hours)'] > 0 ) ]
else:
    if rain_ans=='yes' and snow_ans =='no':
        preferred_cities_df = city_data_df.loc[(city_data_df["Max Temp"] <= max_temp) & (city_data_df["Max Temp"] >= min_temp)& (city_data_df['Rain inches (last 3 hours)'] > 0 ) & (city_data_df['Snow inches (last 3 hours)'] == 0 ) ]
    else:
            if rain_ans=='no' and snow_ans =='yes': 
               preferred_cities_df = city_data_df.loc[(city_data_df["Max Temp"] <= max_temp) & (city_data_df["Max Temp"] >= min_temp)& (city_data_df['Rain inches (last 3 hours)'] == 0 ) & (city_data_df['Snow inches (last 3 hours)'] > 0 ) ]
            else:
                   if rain_ans=='no' and snow_ans =='no':
                       preferred_cities_df = city_data_df.loc[(city_data_df["Max Temp"] <= max_temp) & (city_data_df["Max Temp"] >= min_temp)& (city_data_df['Rain inches (last 3 hours)'] == 0 ) & (city_data_df['Snow inches (last 3 hours)'] == 0 ) ]

preferred_cities_df.head(10)


# %%
# Create DataFrame called hotel_df to store hotel names along with city, country, max temp, and coordinates.
hotel_df = preferred_cities_df[["City", "Country", "Max Temp", "Lat", "Lng",'Current Descrption']].copy()
hotel_df["Hotel Name"] = ""
hotel_df.head(10)


# %%
# Set parameters to search for a hotel.
params = {
    "radius": 5000,
    "type": "lodging",
    "key": gog_key
}


# %%
# Iterate through the DataFrame.
for index, row in hotel_df.iterrows():
    # Get the latitude and longitude.
    lat = row["Lat"]
    lng = row["Lng"]

    # Add the latitude and longitude to the params dictionary as values to the location key.
    params["location"] = f"{lat},{lng}"

    # Use the search term: "lodging" and our latitude and longitude.
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    # Make request and get the JSON data from the search.
    hotels = requests.get(base_url, params=params).json()
    # Grab the first hotel from the results and store the name.
    try:
        hotel_df.loc[index, "Hotel Name"] = hotels["results"][0]["name"]
    except (IndexError):
        print("Hotel not found... skipping.")


# %%
hotel_df.head(10)


# %%
# Add a heatmap of temperature for the vacation spots.
locations = hotel_df[["Lat", "Lng"]]
max_temp = hotel_df["Max Temp"]
fig = gmaps.figure(center=(30.0, 31.0), zoom_level=1.5)
heat_layer = gmaps.heatmap_layer(locations, weights=max_temp, dissipating=False,
             max_intensity=300, point_radius=4)

fig.add_layer(heat_layer)
# Call the figure to plot the data.
fig


# %%
# Add a heatmap of temperature for the vacation spots and marker for each city.
locations = hotel_df[["Lat", "Lng"]]
max_temp = hotel_df["Max Temp"]
fig = gmaps.figure(center=(30.0, 31.0), zoom_level=1.5)
heat_layer = gmaps.heatmap_layer(locations, weights=max_temp,
             dissipating=False, max_intensity=300, point_radius=4)
marker_layer = gmaps.marker_layer(locations)
fig.add_layer(heat_layer)
fig.add_layer(marker_layer)
# Call the figure to plot the data.
fig


# %%
info_box_template = """
<dl>
<dt>Hotel Name</dt><dd>{Hotel Name}</dd>
<dt>City</dt><dd>{City}</dd>
<dt>Country</dt><dd>{Country}</dd>
<dt>Max Temp</dt><dd>{Max Temp} °F</dd>
<dt>Current Description</dt><dd>{Current Descrption}</dd>
</dl>
"""


# %%
# Store the DataFrame Row.
hotel_info = [info_box_template.format(**row) for index, row in hotel_df.iterrows()]


# %%
# Add a heatmap of temperature for the vacation spots and a pop-up marker for each city.
locations = hotel_df[["Lat", "Lng"]]
max_temp = hotel_df["Max Temp"]
fig = gmaps.figure(center=(30.0, 31.0), zoom_level=1.5)
heat_layer = gmaps.heatmap_layer(locations, weights=max_temp,dissipating=False,
             max_intensity=300, point_radius=4)
marker_layer = gmaps.marker_layer(locations, info_box_content=hotel_info)
fig.add_layer(heat_layer)
fig.add_layer(marker_layer)

# Call the figure to plot the data.
fig


# %%
# Create the output file (CSV).
output_data_file = "weather_data/weatherpy_vacation.csv"
# Export the City_Data into a CSV.
hotel_df.to_csv(output_data_file, index_label="City_ID")


# %%


