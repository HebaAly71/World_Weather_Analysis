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
# Create a dataframe for Pacific Grove City
pacgrove_df= vac_data_df[(vac_data_df['City'] == 'Pacific Grove')]
pacgrove_df


# %%
# Create a dataframe for Lompoc City
lompoc_df= vac_data_df[(vac_data_df['City'] == 'Lompoc')]
lompoc_df


# %%
# Create a dataframe for Camarillo City
camarillo_df= vac_data_df[(vac_data_df['City'] == 'Camarillo')]
camarillo_df


# %%
# Create a dataframe for Pahrump City
pahrump_df= vac_data_df[(vac_data_df['City'] == 'Pahrump')]
pahrump_df


# %%
# Configure gmaps to use your Google API key.
gmaps.configure(api_key=gog_key) 


# %%
#  Lat and longitude of Baiao city
pacgrove_latlng= list(zip(pacgrove_df['Lat'],pacgrove_df['Lng']))[0]
pacgrove_latlng


# %%
#  Lat and longitude of Cururupu city
lompoc_latlng= tuple(zip(lompoc_df['Lat'], lompoc_df['Lng']))[0]
lompoc_latlng


# %%
#  Lat and longitude of Camopi city
camarillo_latlng= tuple(zip(camarillo_df['Lat'], camarillo_df['Lng']))[0]
camarillo_latlng


# %%
#  Lat and longitude of Camopi city
pahrump_latlng= tuple(zip(pahrump_df['Lat'], pahrump_df['Lng']))[0]
pahrump_latlng


# %%
fig = gmaps.figure()
pacgrove2pahrump_via_lompoc_camarillo=gmaps.directions_layer(
        pacgrove_latlng, pahrump_latlng, waypoints=[lompoc_latlng, camarillo_latlng],
        travel_mode='DRIVING')
#geneva2zurich_via_montreux = gmaps.directions_layer(
        #geneva, zurich, waypoints=[montreux],
        #travel_mode='Driving')
fig.add_layer(pacgrove2pahrump_via_lompoc_camarillo)
fig
# %%
# Create one dataframe for the four cities
cities_conc= [pacgrove_df,lompoc_df,camarillo_df,pahrump_df]
cities_conc_df=pd.concat(cities_conc)
cities_conc_df
#result = pd.concat(frames)
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
hotel_info = [info_box_template.format(**row) for index, row in cities_conc_df.iterrows()]


# %%
# Add a heatmap of temperature for the vacation spots and a pop-up marker for each city.
locations = cities_conc_df[["Lat", "Lng"]]
max_temp = cities_conc_df["Max Temp"]
fig = gmaps.figure(center=(30.0, 31.0), zoom_level=1.5)
heat_layer = gmaps.heatmap_layer(locations, weights=max_temp,dissipating=False,
             max_intensity=300, point_radius=4)
marker_layer = gmaps.marker_layer(locations, info_box_content=hotel_info)
fig.add_layer(heat_layer)
fig.add_layer(marker_layer)

# Call the figure to plot the data.
fig
# %%


