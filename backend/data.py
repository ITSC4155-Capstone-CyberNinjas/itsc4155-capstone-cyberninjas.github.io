# data.py

'''
Script to handle "querying" and tranformation per client request 

Need to set-up transformation logic in a way that expects raw dataframe 
similar to Snowflake data so that data source can be swapped later 

Task Breakdown:
    read data from file (possibly could read all on to memory in start-up

Will create an object for the data file that will handle reading data and querying

'''
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass
import re 

import pandas as pd
from sklearn import preprocessing as p


@dataclass 
class WiFiData:

    raw_df: pd.DataFrame = None
    queried_df: pd.DataFrame = None
    timelapse_structure: List = None # 3D list needed for folium input
    timestamp_index: List = None # Timestamp index need for folium map timelapse  
    date_pattern: re.Pattern = re.compile(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$') #verifies string is yyyy-mm-dd format 
    buildings: BuildingData = BuildingData().from_csv()


    @classmethod
    def from_csv( cls ):
        df = pd.read_csv( Path('dataset/wifi_counts.csv') )
        df.timestamp = pd.to_datetime(df.timestamp)
        return cls( raw_df = df )    


    @classmethod
    def from_snowflake( cls ):
        pass 

    
    def get_map( self ):
        pass 


    def _query_data( self, date_str: str ):
        # get dataframe subset for given date parameter 

        def _validate_input( q: str ):
            result = re.match( self.date_pattern, q )  # validate string is in format yyyy-mm-dd or yyyy-m-d 
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


    def _format_for_folium( self, subset: pd.DataFrame ):

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

        # normalize data 
        min_max_scaler = p.MinMaxScaler()
        norm_values = min_max_scaler.fit_transform(self.queried_df.values).tolist()

        # create data matrix for map
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
            Create call method so FastAPI knows what to do during dependency injection
            - https://fastapi.tiangolo.com/advanced/advanced-dependencies/ 
        '''
        _query_data( date )
        _format_for_folium( self.queried_df )



@dataclass 
class BuildingData():
    
    raw_df: pd.DataFrame = None 
    buildings_list: List = None
    latitudes_list: List = None
    longitudes_list: List = None
    lat_long_dict: Dict = None


    @classmethod
    def from_csv( cls ):
        
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
        pass 


class DataFactory():
    # TODO: will revisit if this is needed in implementation
    pass
