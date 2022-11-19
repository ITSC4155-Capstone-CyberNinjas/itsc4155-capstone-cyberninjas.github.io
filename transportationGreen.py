import folium
from folium import plugins
import pandas as pd
from folium.plugins import HeatMap
import folium.plugins as plugins
from folium.plugins import HeatMapWithTime
from folium.plugins import Search

#base_df=pd.read_csv(r"C:\Users\Administrator\Downloads\Sample Locations.csv")
base_df = pd.read_csv("csv/TransitSamplesGreen.csv")
base_df.head()

# created map from folium
OurMap = folium.Map(location=[35.30742034864125, -80.73590951022354], tiles="OpenStreetMap", zoom_start=15, control_scale=True) 

# needed for time lapse
time_index = list(base_df['Timestamp'].sort_values().astype('str').unique())
time_index

base_df['Timestamp'] = base_df['Timestamp'].sort_values(ascending=True)
data = []
for _, d in base_df.groupby('Timestamp'):
    data.append([[row['Latitude'], row['Longitude'], row['Count']]
                for _, row in d.iterrows()])
data

# timelapse heat map
HeatMapWithTime(data,
                index=time_index,
                auto_play=True,
                radius=65,
                position='bottomright',
                use_local_extrema=True,
                ).add_to(OurMap)

heat_weight = list(map(list, zip(base_df["Latitude"],
                                 base_df["Longitude"],
                                 base_df["Count"]
                                 )
                       )
                   )
heat_weight[:5]

# setting up search feature
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
        "Stop": d[1]["Stop"], 
      }
    }
    geo_json["features"].append(temp_dict),
geojson_obj = folium.GeoJson(geo_json).add_to(OurMap)

# for loop to iterate trhoug the data frame and create markers
for i, r in base_df.iterrows():
    tooltip = (r['Stop'])
    folium.Marker(
        location=[r['Latitude'], r['Longitude']],
        tooltip=tooltip,
        popup=(r['Count'], r'Humans On Bus'),
        icon=folium.Icon(markerColor="green"),
    ).add_to(OurMap)

# search bar that returns the Stop of building
servicesearch = Search(
    layer=geojson_obj,
    search_label="Stop",
    position="topright",
    search_zoom=17,
    placeholder='Search for a Stop        ',
    collapsed=False,
).add_to(OurMap)

# adding everything to folium map
HeatMap(heat_weight).add_to(OurMap)
OurMap
OurMap.save("foliumTransportGreen.html")

# search function
# https://stackoverflow.com/questions/63581614/python-folium-search-plugin-doesnt-search-popup-text-in-markercluster-group-l
# Folium Plugings https://python-visualization.github.io/folium/plugins.html


#-----------------..............--------------...................----------------.................
# OLD CRAP! COMMENTING OUT FOR SHITS AND GIGGLES!!!


# import folium

# from folium.plugins import HeatMap

# map = folium.Map(location=[35.30815951601069, -80.73284919823239], tiles="OpenStreetMap", zoom_start = 15)

# # legend for heathmap
# less = 0.7
# moderate = 0.9
# crowded = 1

# data = [

#    [35.30243780204842, -80.7375250398117, less], # Alumni Way East
#    [35.308067793700964, -80.73043103761148, moderate], # Auxilary Services
#    [35.31035043727518, -80.73614250635478, crowded], # Belk Hall
#    [35.30503067188768, -80.72809791721689, less], # Cato Hall North
#    [35.305119133356385, -80.72827857918276, moderate], # Cato Hall South
#    [35.304322976630644, -80.73457077757303, crowded], # Cone Deck
#    [35.3116802713624, -80.73040951411953, less], # FM/PPS
#    [35.30735591268372, -80.72929544799972, moderate], # Fretwell North
#    [35.30691361660144, -80.72946578642468, crowded], # Fretwell South
#    [35.301902801569426, -80.73281750500189, less], # Gage UA Center
#    [35.311978970054014, -80.73375015765203, moderate], # Light Rail West
#    [35.31339200503512, -80.73197372222752, crowded], # North Deck
#    [35.304369314007296, -80.73270221658669, less], # Reese West
#    [35.30340886113664, -80.72939868338558, moderate], # Robinson Hall North
#    [35.303707950761805, -80.72943481577379, crowded], # Robinson Hall South
#    [35.30109818790611, -80.73583197907419, less], # South Village Deck
#    [35.31061038910347, -80.72923779212933, moderate], # Student Health North
#    [35.30815951601069, -80.73284919823239, crowded] # Student Union East
# ]

# HeatMap(data).add_to(map)

# folium.Marker(
#    [35.30243780204842, -80.7375250398117], tooltip="Alumni Way East"
# ).add_to(map)
# folium.Marker(
#    [35.308067793700964, -80.73043103761148], tooltip="Auxilary Services"
# ).add_to(map)
# folium.Marker(
#    [35.31035043727518, -80.73614250635478], tooltip="Belk Hall"
# ).add_to(map)
# folium.Marker(
#    [35.30503067188768, -80.72809791721689], tooltip="Cato Hall North"
# ).add_to(map)
# folium.Marker(
#    [35.305119133356385, -80.72827857918276], tooltip="Cato Hall South"
# ).add_to(map)
# folium.Marker(
#    [35.304322976630644, -80.73457077757303], tooltip="Cone Deck"
# ).add_to(map)
# folium.Marker(
#    [35.3116802713624, -80.73040951411953], tooltip="FM/PPS"
# ).add_to(map)
# folium.Marker(
#    [35.30735591268372, -80.72929544799972], tooltip="Fretwell North"
# ).add_to(map)
# folium.Marker(
#    [35.30691361660144, -80.72946578642468], tooltip="Fretwell South"
# ).add_to(map)
# folium.Marker(
#    [35.301902801569426, -80.73281750500189], tooltip="Gage UA Center"
# ).add_to(map)
# folium.Marker(
#    [35.311978970054014, -80.73375015765203], tooltip="Light Rail West"
# ).add_to(map)
# folium.Marker(
#    [35.31339200503512, -80.73197372222752], tooltip="North Deck"
# ).add_to(map)
# folium.Marker(
#    [35.304369314007296, -80.73270221658669], tooltip="Reese West"
# ).add_to(map)
# folium.Marker(
#    [35.30340886113664, -80.72939868338558], tooltip="Robinson Hall North"
# ).add_to(map)
# folium.Marker(
#    [35.303707950761805, -80.72943481577379], tooltip="Robinson Hall South"
# ).add_to(map)
# folium.Marker(
#    [35.30109818790611, -80.73583197907419], tooltip="South Village Deck"
# ).add_to(map)
# folium.Marker(
#    [35.31061038910347, -80.72923779212933], tooltip="Student Health North"
# ).add_to(map)
# folium.Marker(
#    [35.30815951601069, -80.73284919823239], tooltip="Student Union East"
# ).add_to(map)

# map.save("foliumTransportGreen.html")

# # Green Route Bus Stop Names

# # Alumni Way East
# # Auxilary Services
# # Belk Hall
# # Cato Hall North
# # Cato Hall South
# # Cone Deck
# # FM/PPS
# # Fretwell North
# # Fretwell South
# # Gage UA Center
# # Light Rail
# # North Deck
# # Reese West
# # Robinson Hall North
# # Robinson Hall South
# # South Village Deck
# # Student Health North
# # Student Union East