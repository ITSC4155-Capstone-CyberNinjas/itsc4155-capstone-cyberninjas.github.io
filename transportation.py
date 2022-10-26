import folium

from folium.plugins import HeatMap

map = folium.Map(location=[35.30742034864125, -80.73590951022354], tiles="OpenStreetMap", zoom_start = 15)

# legend for heathmap
less = 0.7
moderate = 0.9
crowded = 1

data = [

   [35.30589304115362, -80.73214474067815, less], # Atkins
   [35.30630234706238, -80.7344093006642, moderate], # Barnard
   [35.305400523040255, -80.73552509953846, crowded], # Belk Gymnasium
   [35.31267640715162, -80.74200998338922, less], # Bioinformatics
   [35.307534535678194, -80.73236613083795, moderate], # Burson
   [35.3077865349813, -80.73119368119363, crowded], # Cameron Hall
   [35.30550548981937, -80.72873019682216, less], # Cato College of Education
   [35.30741563950016, -80.73335442877301, moderate], # College of Health and Human Services
   [35.30460541601236, -80.73173933083798, crowded], # Colvard
   [35.30546443648395, -80.72984370200263, less], # Denny
   [35.311936203433405, -80.74128874194673, moderate], # Duke Centennial Hall
   [35.30910488607636, -80.7434065042412, crowded], # Early College Highschool
   [35.309025939422504, -80.74162792370868, less], # EPIC
   [35.30605569666243, -80.72906331158887, moderate], # Fretwell
   [35.306300543492895, -80.72992922150952, crowded], # Friday
   [35.3049591469742, -80.72973315838593, less], # Garinger
   [35.31131404665103, -80.74198147619241, moderate], # Grigg
   [35.303894812664105, -80.72879863677528, crowded], # Johnson Band Center
   [35.312289175288136, -80.7407199673467, less], # Kulwicki Motorsports Laboratory
   [35.30569919531408, -80.73041129093589, moderate], # Macy
   [35.307108128109746, -80.73001691547567, crowded], # McEniry
   [35.30776970361139, -80.7296816258644, less], # McMillan Greenhouse
   [35.312633472097744, -80.74026908543213, moderate],# Motorsport Research
   [35.31164386878899, -80.74298120264842, crowded], # Portal
   [35.303453157479574, -80.72993034023219, less], # Robinson Hall
   [35.30461111317007, -80.73077113083795, moderate], # Rowe
   [35.308383668762346, -80.73014622006914, crowded], # Science Building
   [35.306891540723925, -80.73157816033924, less], # Smith
   [35.304630385739735, -80.7291291992021, moderate], # Storrs
   [35.30513675406152, -80.73041915648714, crowded], # Winningham
   [35.307515862770785, -80.73571705830427, less] # Woodward Hall
]

HeatMap(data).add_to(map)

folium.Marker(
   [35.30589304115362, -80.73214474067815], tooltip="Atkins"
).add_to(map)
folium.Marker(
   [35.30630234706238, -80.7344093006642], tooltip="Barnard"
).add_to(map)
folium.Marker(
   [35.305400523040255, -80.73552509953846], tooltip="Belk Gymnasium"
).add_to(map)
folium.Marker(
   [35.31267640715162, -80.74200998338922], tooltip="Bioinformatics"
).add_to(map)
folium.Marker(
   [35.307534535678194, -80.73236613083795], tooltip="Burson"
).add_to(map)
folium.Marker(
   [35.3077865349813, -80.73119368119363], tooltip="Cameron Hall"
).add_to(map)
folium.Marker(
   [35.30550548981937, -80.72873019682216], tooltip="College of Health and Human Services"
).add_to(map)
folium.Marker(
   [35.30460541601236, -80.73173933083798], tooltip="Colvard"
).add_to(map)
folium.Marker(
   [35.30546443648395, -80.72984370200263], tooltip="Denny"
).add_to(map)
folium.Marker(
   [35.311936203433405, -80.74128874194673], tooltip="Duke Centennial Hall"
).add_to(map)
folium.Marker(
   [35.30910488607636, -80.7434065042412], tooltip="Early College Highschool"
).add_to(map)
folium.Marker(
   [35.309025939422504, -80.74162792370868], tooltip="Epic"
).add_to(map)
folium.Marker(
   [35.30605569666243, -80.72906331158887], tooltip="Fretwell"
).add_to(map)
folium.Marker(
   [35.306300543492895, -80.72992922150952], tooltip="Friday"
).add_to(map)
folium.Marker(
   [35.3049591469742, -80.72973315838593], tooltip="Garinger"
).add_to(map)
folium.Marker(
   [35.31131404665103, -80.74198147619241], tooltip="Grigg"
).add_to(map)
folium.Marker(
   [35.303894812664105, -80.72879863677528], tooltip="Johnson Band Center"
).add_to(map)
folium.Marker(
   [35.312289175288136, -80.7407199673467], tooltip="Kulwicki Motorsports Laboratory"
).add_to(map)
folium.Marker(
   [35.30569919531408, -80.73041129093589], tooltip="Macy"
).add_to(map)
folium.Marker(
   [35.307108128109746, -80.73001691547567], tooltip="McEniry"
).add_to(map)
folium.Marker(
   [35.30776970361139, -80.7296816258644], tooltip="McMillan Greenhouse"
).add_to(map)
folium.Marker(
   [35.312633472097744, -80.74026908543213], tooltip="Motorsport Research"
).add_to(map)
folium.Marker(
   [35.31164386878899, -80.74298120264842], tooltip="Portal"
).add_to(map)
folium.Marker(
   [35.303453157479574, -80.72993034023219], tooltip="Robinson Hall"
).add_to(map)
folium.Marker(
   [35.30461111317007, -80.73077113083795], tooltip="Rowe"
).add_to(map)
folium.Marker(
   [35.308383668762346, -80.73014622006914], tooltip="Science Building"
).add_to(map)
folium.Marker(
   [35.306891540723925, -80.73157816033924], tooltip="Smith"
).add_to(map)
folium.Marker(
   [35.304630385739735, -80.7291291992021], tooltip="Storrs"
).add_to(map)
folium.Marker(
   [35.30513675406152, -80.73041915648714], tooltip="Winningham"
).add_to(map)
folium.Marker(
   [35.307515862770785, -80.73571705830427], tooltip="Woodward Hall"
).add_to(map)

map.save("foliumTransport.html")

# Buildings lat, long, and name
# [35.30589304115362, -80.73214474067815] Atkins
# [35.30630234706238, -80.7344093006642] Barnard
# [35.305400523040255, -80.73552509953846] Belk Gymnasium
# [35.31267640715162, -80.74200998338922] Bioinformatics
# [35.307534535678194, -80.73236613083795] Burson
# [35.3077865349813, -80.73119368119363] Cameron Hall
# [35.30550548981937, -80.72873019682216] Cato College of Education
# [35.30741563950016, -80.73335442877301] College of Health and Human Services
# [35.30460541601236, -80.73173933083798] Colvard
# [35.30546443648395, -80.72984370200263] Denny
# [35.311936203433405, -80.74128874194673] Duke Centennial Hall
# [35.30910488607636, -80.7434065042412] Early College Highschool
# [35.309025939422504, -80.74162792370868] EPIC
# [35.30605569666243, -80.72906331158887] Fretwell
# [35.306300543492895, -80.72992922150952] Friday
# [35.3049591469742, -80.72973315838593] Garinger
# [35.31131404665103, -80.74198147619241] Grigg
# [35.303894812664105, -80.72879863677528] Johnson Band Center
# [35.312289175288136, -80.7407199673467] Kulwicki Motorsports Laboratory
# [35.30569919531408, -80.73041129093589] Macy
# [35.307108128109746, -80.73001691547567] McEniry
# [35.30776970361139, -80.7296816258644] McMillan Greenhouse
# [35.312633472097744, -80.74026908543213] Motorsport Research
# [35.31164386878899, -80.74298120264842] Portal
# [35.303453157479574, -80.72993034023219] Robinson Hall
# [35.30461111317007, -80.73077113083795] Rowe
# [35.308383668762346, -80.73014622006914] Science Building
# [35.306891540723925, -80.73157816033924] Smith
# [35.304630385739735, -80.7291291992021] Storrs
# [35.30513675406152, -80.73041915648714] Winningham
# [35.307515862770785, -80.73571705830427] Woodward Hall