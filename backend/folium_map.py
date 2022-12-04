# map.py

'''
script for handling folium map generation 
'''

from pathlib import Path

import folium
from folium.plugins import HeatMap, HeatMapWithTime, Search

UNCC_COORDINATES = [35.30742034864125, -80.73590951022354]

class Map:

	def __init__( self, map_type: str ):
		self.map_type = map_type  #TODO: may need logic later based on map type
		self.base_map = folium.Map( 
			location= UNCC_COORDINATES, 
			tiles="OpenStreetMap", 
			zoom_start=15,
			 control_scale=True 
		) 


	def generate_heatmap_timelapse( self, data: list, index: list ):
		HeatMapWithTime( 
			data, 
			index = index, 
			radius = 50
		).add_to(self.base_map)


	def generate_search_markers( self ):
		pass


	def get_map( self ):
		return self.base_map
	
	def write_map( self ):
		# TODO
		p = Path('/home/calvin/capstone/itsc4155-capstone-cyberninjas.github.io/wifi_map.html')
		self.base_map.save( p )
		return p