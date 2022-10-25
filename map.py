import folium

from folium.plugins import HeatMap

map = folium.Map(location=[35.30742034864125, -80.73590951022354], tiles="OpenStreetMap", zoom_start = 15)

data = [
   [35.307515862770785, -80.73571705830427], # Woodward Hall
   [35.31267640715162, -80.74200998338922], # Bioinformatics
   [35.30550548981937, -80.72873019682216], # Cato
   [35.30589304115362, -80.73214474067815], #J. Murrey Atkins Library
   [35.3077865349813, -80.73119368119363], # Cameron
   [35.31052012671641, -80.72956218797971] # Student Health Center
]

HeatMap(data).add_to(map)
map.save("folium.html")