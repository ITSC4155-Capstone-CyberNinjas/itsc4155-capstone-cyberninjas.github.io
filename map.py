import folium

from folium.plugins import HeatMap

map = folium.Map(location=[35.303555, -80.73238], tiles="OpenStreetMap", zoom_start = 15)

data = [
    [35.307634, -80.733623]
]

HeatMap(data).add_to(map)
map.save("folium.html")