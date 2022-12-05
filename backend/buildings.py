# buildings.py

'''
    Script for handling building data
'''

from pathlib import Path
from dataclasses import dataclass

import pandas as pd


@dataclass 
class BuildingData():
    
    raw_df: pd.DataFrame = None 
    buildings_list: list = None
    latitudes_list: list = None
    longitudes_list: list = None
    lat_long_dict: dict = None


    @classmethod
    def from_csv( cls ):
        
        #TODO: env variabales for paths
        df = pd.read_csv( Path('dataset/buildings.csv') ).dropna() 
        
        buildings_list = list( df['Building abbreviation'] )
        latitudes_list = list( df['Latitude'] )
        longitudes_list = list( df['Longitude'] )
        
        lat_long_dict = { 
            k:v for k,v in zip( buildings_list, zip( latitudes_list, longitudes_list ) ) 
        }

        # convert dictionary values to list (instead of tuple)
        for k in lat_long_dict.keys():
            lat_long_dict[k] = list( lat_long_dict[k] )
        
        return cls(
            raw_df = df,
            buildings_list = buildings_list,
            latitudes_list = latitudes_list,
            longitudes_list = longitudes_list,
            lat_long_dict = lat_long_dict
        )


    @classmethod
    def from_snowflake( cls ):
        # TODO
        pass 