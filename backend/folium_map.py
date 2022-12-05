# folium_map.py

'''
	Script for handling folium map generation 
'''

from pathlib import Path

import folium
from folium.plugins import HeatMap, HeatMapWithTime, Search

from buildings import BuildingData

# center point for map
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
		self.buildings = BuildingData().from_csv()


	def create_heatmap_timelapse( self, data: list, index: list ):
		'''
			Create heatmap with timelapse using folium plug-in
		'''
		HeatMapWithTime( 
			data, 
			index = index, 
			radius = 50
		).add_to(self.base_map)


	def create_search_markers( self ):
		#TODO: parameterize this per map_type (wifi vs transit have different search items)


		'''
			Add "building search" function to the heatmap using folium plug-in
		'''
		def _setup_geojson():
			'''
				Set-up geojson object for search plug-in
			'''
			
			geo_json = {
			  "type": "FeatureCollection",
			  "features": []
			}
			for b in self.buildings.raw_df.iterrows():
			    temp_dict = {
			    	"type": "Feature",
			      	"geometry": {
				        "type": "Point",
				        "coordinates":[b[1]["Longitude"], b[1]["Latitude"]]
			    	},
			    	"properties": {
			    		"Name": b[1]["Building Name"], 
			    	}
			    }
			    geo_json["features"].append( temp_dict )

			return geo_json


		search = folium.FeatureGroup( name="Search", show=False ).add_to( self.base_map )
		
		geojson_obj = folium.GeoJson(
			_setup_geojson(), 
			zoom_on_click=True
		).add_to( search )

		Search(
		    layer=geojson_obj,
		    search_label="Name",
		    geom_type="Point",
		    search_zoom = 17,
		    position="topright",
		    placeholder="Search for a building",
		    collapsed=False
		).add_to( self.base_map )

		folium.LayerControl().add_to( self.base_map )


	def get_map( self ):
		'''
		Return folium.Map object
		'''
		return self.base_map
	

	def write_map( self ):
		# TODO: env var for path 
		p = Path('wifi_map.html')
		self.base_map.save( p )
		return p