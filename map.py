import folium
from folium import plugins
import pandas as pd
from folium.plugins import HeatMap
import folium.plugins as plugins
from folium.plugins import HeatMapWithTime
from folium.plugins import Search

#base_df=pd.read_csv(r"C:\Users\Administrator\Downloads\Sample Locations.csv")
base_df = pd.read_csv("SampleLocations.csv")
base_df.head()

OurMap = folium.Map(location=[35.30742034864125, -80.73590951022354], tiles="OpenStreetMap", zoom_start=15, control_scale=True) 

time_index = list(base_df['Timestamp'].sort_values().astype('str').unique())
time_index

base_df['Timestamp'] = base_df['Timestamp'].sort_values(ascending=True)
data = []
for _, d in base_df.groupby('Timestamp'):
    data.append([[row['Latitude'], row['Longitude'], row['Count']]
                for _, row in d.iterrows()])
data

HeatMapWithTime(data,
                index=time_index,
                auto_play=False,
                use_local_extrema=True, 
                ).add_to(OurMap)

heat_weight = list(map(list, zip(base_df["Latitude"],
                                 base_df["Longitude"],
                                 base_df["Count"]
                                 )
                       )
                   )
heat_weight[:5]

geo_json = {
  "type": "FeatureCollection",
  "features": [],
}
for d in base_df.iterrows():
    temp_dict = {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates":[d[1]["Longitude"], d[1]["Latitude"]],
      },
      "properties": {
        "Name": d[1]["Name"], 
      }
    }
    geo_json["features"].append(temp_dict),
geojson_obj = folium.GeoJson(geo_json).add_to(OurMap)

for i, r in base_df.iterrows():
    tooltip = (r['Name'])
    folium.Marker(
        location=[r['Latitude'], r['Longitude']],
        tooltip=tooltip,
        popup=(r['Count'], r'Devices'),
        icon=folium.Icon(markerColor="green"),
    ).add_to(OurMap)

servicesearch = Search(
    layer=geojson_obj,
    search_label="Name",
    position="topright",
    placeholder='Search for a building        ',
    collapsed=False,
).add_to(OurMap)

HeatMap(heat_weight).add_to(OurMap)
OurMap
OurMap.save("folium.html")

# search function
# https://stackoverflow.com/questions/63581614/python-folium-search-plugin-doesnt-search-popup-text-in-markercluster-group-l
# Folium Plugings https://python-visualization.github.io/folium/plugins.html