import folium
from folium import plugins
import pandas as pd
from folium.plugins import HeatMap
import folium.plugins as plugins
from folium.plugins import HeatMapWithTime
from folium.plugins import Search

#base_df=pd.read_csv(r"C:\Users\Administrator\Downloads\Sample Locations.csv")
base_df = pd.read_csv("csv/TransitSamplesSilver.csv")
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
    placeholder='Search for a Stop        ',
    collapsed=False,
).add_to(OurMap)

# adding everything to folium map
HeatMap(heat_weight).add_to(OurMap)
OurMap
OurMap.save("foliumTransportSilver.html")

# search function
# https://stackoverflow.com/questions/63581614/python-folium-search-plugin-doesnt-search-popup-text-in-markercluster-group-l
# Folium Plugings https://python-visualization.github.io/folium/plugins.html


#-----------------..............--------------...................----------------.................
# OLD CRAP! COMMENTING OUT FOR SHITS AND GIGGLES!!!

# import folium

# from folium.plugins import HeatMap

# map = folium.Map(location=[35.30794215338082, -80.73511035782593], tiles="OpenStreetMap", zoom_start = 15)

# # legend for heathmap
# less = 0.7
# moderate = 0.9
# crowded = 1

# data = [

#    [35.307469363314084, -80.74017436838038, less], # Athletics Complex East
#    [35.307600694176486, -80.73999197817976, moderate], # Athletics Complex West
#    [35.30806472816382, -80.73034675466805, crowded], # Auxiliary Services
#    [35.309194158319045, -80.7443908006883, less], # CRI Deck
#    [35.31238974733628, -80.74162276121262, moderate], # Duke Centennial Hall
#    [35.30627862039809, -80.72702081550266, crowded], # East Deck 2
#    [35.30935175199663, -80.74119360779945, less], # EPIC North
#    [35.31018349117011, -80.74196608394318, moderate], # EPIC South
#    [35.30735591268372, -80.72929544799972, crowded], # Fretwell North
#    [35.31104148682978, -80.74147255751802, less], # Grigg Hall
#    [35.30723296719705, -80.72529347294817, moderate], # Lot 5A
#    [35.30870386497582, -80.72511108274757, crowded], # Lot 6
#    [35.31040236845253, -80.72705300200938, less], # Martin Hall
#    [35.312792470141545, -80.74091465808088, moderate], # Motorsports
#    [35.31122534185856, -80.74297459446416, crowded], # Portal West
#    [35.308196058059686, -80.73031456816206, less], # Science Building
#    [35.31042863370326, -80.72913439624001, moderate], # Student Health North
#    [35.3080472174944, -80.73279292927869, crowded], # Student Union East
#    [35.30823983464373, -80.73268564092538, crowded] # Student Union West
# ]

# HeatMap(data).add_to(map)

# folium.Marker(
#    [35.307469363314084, -80.74017436838038], tooltip="Athletics Complex East"
# ).add_to(map)
# folium.Marker(
#    [35.307600694176486, -80.73999197817976], tooltip="Athletics Complex West"
# ).add_to(map)
# folium.Marker(
#    [35.30806472816382, -80.73034675466805], tooltip="Auxiliary Services"
# ).add_to(map)
# folium.Marker(
#    [35.309194158319045, -80.7443908006883], tooltip="CRI Deck"
# ).add_to(map)
# folium.Marker(
#    [35.31238974733628, -80.74162276121262], tooltip="Duke Centennial Hall"
# ).add_to(map)
# folium.Marker(
#    [35.30627862039809, -80.72702081550266], tooltip="East Deck 2"
# ).add_to(map)
# folium.Marker(
#    [35.30935175199663, -80.74119360779945], tooltip="EPIC North"
# ).add_to(map)
# folium.Marker(
#    [35.31018349117011, -80.74196608394318], tooltip="Epic South"
# ).add_to(map)
# folium.Marker(
#    [35.30735591268372, -80.72929544799972], tooltip="Fretwell North"
# ).add_to(map)
# folium.Marker(
#    [35.31104148682978, -80.74147255751802], tooltip="Grigg Hall"
# ).add_to(map)
# folium.Marker(
#    [35.30723296719705, -80.72529347294817], tooltip="Lot 5A"
# ).add_to(map)
# folium.Marker(
#    [35.30870386497582, -80.72511108274757], tooltip="Lot 6"
# ).add_to(map)
# folium.Marker(
#    [35.31040236845253, -80.72705300200938], tooltip="Martin Hall"
# ).add_to(map)
# folium.Marker(
#    [35.312792470141545, -80.74091465808088], tooltip="Motorsports"
# ).add_to(map)
# folium.Marker(
#    [35.31122534185856, -80.74297459446416], tooltip="Portal West"
# ).add_to(map)
# folium.Marker(
#    [35.308196058059686, -80.73031456816206], tooltip="Science Building"
# ).add_to(map)
# folium.Marker(
#    [35.31042863370326, -80.72913439624001], tooltip="Student Health North"
# ).add_to(map)
# folium.Marker(
#    [35.3080472174944, -80.73279292927869], tooltip="Student Union East"
# ).add_to(map)
# folium.Marker(
#    [35.30823983464373, -80.73268564092538], tooltip="Student Union West"
# ).add_to(map)

# map.save("foliumTransportSilver.html")

# # Silver Route Bus Stop Stops

# # Athletics Complex East
# # Athletics Complex West
# # Auxiliary Services
# # CRI Deck
# # Duke Centennial Hall
# # East Deck 2
# # EPIC North
# # EPIC South
# # Fretwell North
# # Grigg Hall
# # Lot 5A
# # Lot 6
# # Martin Hall
# # Motorsports
# # Portal West
# # Science Building
# # Student Health North
# # Student Union East
# # Student Union West