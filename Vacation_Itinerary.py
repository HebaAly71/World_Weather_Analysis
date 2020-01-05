# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Import the dependencies.
import pandas as pd
import gmaps
import requests
import gmaps.datasets

# %%
# Import the API key.
from config import gog_key


# %%
# Store the CSV you saved created in part one into a DataFrame.
vac_data_df = pd.read_csv("weather_data/weatherpy_vacation.csv")
vac_data_df.head()
# %%
# Create a dataframe for Cururupu City
cururupu_df= vac_data_df[(vac_data_df['City'] == 'Cururupu')]
cururupu_df
# %%
# Create a dataframe for Baiao City
baiao_df= vac_data_df[(vac_data_df['City'] == 'Baiao')]
baiao_df
# %%
# Create a dataframe for Camopi City
camopi_df= vac_data_df[(vac_data_df['City'] == 'Camopi')]
camopi_df
# %%
# Create a dataframe for Sinnamary City
sinnamary_df= vac_data_df[(vac_data_df['City'] == 'Sinnamary')]
sinnamary_df
# %%
# Configure gmaps to use your Google API key.
gmaps.configure(api_key=gog_key) 
# %%
#  Lat and longitude of Baiao city
baiao_latlng= list(zip(baiao_df['Lat'],baiao_df['Lng']))[0]
baiao_latlng
# %%
#  Lat and longitude of Cururupu city
cururupu_latlng= tuple(zip(cururupu_df['Lat'], cururupu_df['Lng']))[0]
cururupu_latlng
# %%
#  Lat and longitude of Camopi city
sinnamary_latlng= tuple(zip(sinnamary_df['Lat'], sinnamary_df['Lng']))[0]
sinnamary_latlng
# %%
#  Lat and longitude of Camopi city
camopi_latlng= tuple(zip(camopi_df['Lat'], camopi_df['Lng']))[0]
camopi_latlng
# %%
fig = gmaps.figure()
sinnamary2cururupu_via_camopi_baiao=gmaps.directions_layer(
        sinnamary_latlng, cururupu_latlng, waypoints=[baiao_latlng, camopi_latlng],
        travel_mode='DRIVING')
#geneva2zurich_via_montreux = gmaps.directions_layer(
        #geneva, zurich, waypoints=[montreux],
        #travel_mode='Driving')
fig.add_layer(sinnamary2cururupu_via_camopi_baiao)
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


