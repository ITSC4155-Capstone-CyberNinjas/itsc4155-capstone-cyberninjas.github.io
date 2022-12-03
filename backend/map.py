# map.py

'''
script for handling folium map generation 
'''

import folium
from folium.plugins import HeatMap, HeatMapWithTime, Search

UNCC_COORDINATES = [35.30742034864125, -80.73590951022354]

class Map:

	def __init__( map_type: str ):
		self.map_type = map_type  
		self.base_map = folium.Map( 
			location= UNCC_COORDINATES, 
			tiles="OpenStreetMap", 
			zoom_start=15,
			 control_scale=True 
		) 


	def generate_heatmap_timelapse( self ):
		pass


	def generate_search_markers( self ):
		pass


	def 





	