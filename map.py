import folium
from folium import plugins
import pandas as pd
from folium.plugins import HeatMap
import folium.plugins as plugins
import requests
import time
from folium.plugins import HeatMapWithTime
import datetime
import numpy as np

#base_df=pd.read_csv(r"C:\Users\Administrator\Downloads\Sample Locations.csv")
base_df=pd.read_csv("SampleLocations.csv")
base_df.head()

OurMap = folium.Map(location=[35.30742034864125, -80.73590951022354], tiles="OpenStreetMap", zoom_start = 15)

heat_weight = list(map(list,zip(base_df["Latitude"],
                          base_df["Longitude"],
                          base_df["Count"]
                          )
                 )
            )
heat_weight[:5]

for i, r in base_df.iterrows():
    #setting for the popup
    #popup=folium.Popup(r['Name'], max_width=10000)
    tooltip=(r['Name'])
    #Plotting the Marker for each building
    folium.map.Marker(
        location=[r['Latitude'], r['Longitude']], 
        tooltip=tooltip,
        popup=(r['Count'], r'Devices'),
        icon=folium.Icon(color="green", icon="university")
    ).add_to(OurMap)
    
#HeatMap(heat_weight).add_to(OurMap)
#OurMap

time_index = list(base_df['Timestamp'].sort_values().astype('str').unique())
time_index

base_df['Timestamp'] = base_df['Timestamp'].sort_values(ascending=True)
data = []
for _, d in base_df.groupby('Timestamp'):
    data.append([[row['Latitude'], row['Longitude'], row['Count']] for _, row in d.iterrows()])
data

HeatMapWithTime(data,
                index=time_index,
                auto_play=True,
                use_local_extrema=True
               ).add_to(OurMap)

HeatMap(heat_weight).add_to(OurMap)
OurMap
OurMap.save("folium.html")