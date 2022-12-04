# data.py

'''
    This script contains classes for handling WiFi and Transit data as needed. 
    These classes facilitate queries and tranformations. They are set-up to be 
    injected as dependencies in the path functions (main.py)
'''

from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass
import re 

import pandas as pd
from sklearn import preprocessing as p
from fastapi import HTTPException

from folium_map import Map
from buildings import BuildingData


@dataclass 
class WiFiData:

    raw_df: pd.DataFrame = None
    queried_df: pd.DataFrame = None
    timelapse_structure: list = None # 3D list needed for folium input
    timestamp_index: list = None # Timestamp index need for folium map timelapse  
    date_pattern: re.Pattern = re.compile(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$') #verifies string is yyyy-mm-dd format 
    buildings: BuildingData = BuildingData().from_csv()


    @classmethod
    def from_csv( cls ):
        '''
        Read raw data from csv
        '''

        #TODO: environ variables for local paths
        df = pd.read_csv( Path('backend/dataset/wifi_counts.csv') )
        df.timestamp = pd.to_datetime(df.timestamp)
        return cls( raw_df = df )    


    @classmethod
    def from_snowflake( cls ):
        # TODO: snowflake connector script
        pass 

    
    def get_map( self ):
        '''
        Get folium.Map instance from folium_map script
        '''

        _map = Map('wifi')
        _map.generate_heatmap_timelapse(self.timelapse_structure, self.timestamp_index)
        _map.generate_search_markers()
        
        return _map


    def _query_data( self, date_str: str ):
        '''
        Given a date (yyyy-mm-dd), query the data for all records within the date
        '''

        def _validate_input( q: str ):
            '''
            Validate the date string is in correct format (yyyy-mm-dd) and convert to datetime object
            '''

            result = re.match( self.date_pattern, q )  
            if result is None:
                raise HTTPException( 
                    status_code = 400, 
                    detail = "Invalid string format for date. Should be formatted as yyyy-mm-dd" 
                )
            else:
                y_m_d = [ int(x) for x in q.split('-') ]
                return datetime( year = y_m_d[0], month = y_m_d[1], day = y_m_d[2] )
         

        date = _validate_input( date_str )
        query = f"timestamp >= '{date}' and timestamp < '{date + timedelta(1)}'"
        
        self.queried_df = self.raw_df.query( query ).copy()

        if len(self.queried_df) == 0:
            raise HTTPException(
                status_code = 500,
                detail = "No data for given date"
            )
        


    def _format_for_folium( self ):
        '''
        Once data has been queried, perform transformations to match folium specs
        '''

        if self.queried_df is None:
            raise HTTPException(
                status_code = 500,
                detail = 'No query to format for Folium'
            )

        # index for folium to loop over
        self.timestamp_index = [ str(x) for x in pd.to_datetime(self.queried_df.timestamp) ]

        #drop building with nulls from data
        curr_cols = set( self.queried_df.columns )
        to_keep = set( self.buildings.buildings_list )
        to_drop = list( curr_cols.difference(to_keep) )
        self.queried_df.drop( columns = to_drop, inplace = True )

        # Folium expects values between 0 and 1
        norm_values = p.Normalizer(norm = 'max').transform( self.queried_df.values ).tolist()

        # create data matrix for folium map
        self.timelapse_structure = []
        for row in norm_values:
            new_row = []
            for idx, col in enumerate( self.queried_df.columns ):
                curr_coordinate = self.buildings.lat_long_dict[col].copy()
                curr_coordinate.append( row[idx] )
                new_row.append( 
                    curr_coordinate
                )
            self.timelapse_structure.append( new_row )
        

    def __call__( self, date: str ):
        '''
        Created call method so FastAPI knows what to do during dependency injection
            - https://fastapi.tiangolo.com/advanced/advanced-dependencies/ 
        '''
        self._query_data( date )
        self._format_for_folium()


    def __hash__(self):
        '''
        objects need to be hashable for FastAPI dependency cache
        '''
        return hash(repr(self))



class DataFactory():
    # TODO: will revisit if this is needed in implementation
    pass
