import folium

map = folium.Map(location=[35.303555, -80.73238], tiles="OpenStreetMap", zoom_start = 15)

map.save("folium.html")