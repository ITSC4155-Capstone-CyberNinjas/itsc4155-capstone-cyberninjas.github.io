# data.py

'''
Script to handle "querying" and tranformation per client request 

Need to set-up transformation logic in a way that expects raw dataframe 
similar to Snowflake data so that data source can be swapped later 

Task Breakdown:
    read data from file (possibly could read all on to memory in start-up

Will create an object for the data file that will handle reading data and querying

'''
from abc import ABC, abstractmethod
from pathlib import Path
from datetime import datetime, timedelta

import pandas as pd


#defining a Base Class since we have multiple data files 
class BaseData(ABC):

    @abstractmethod
    def read_data():
        ...

    @abstractmethod
    def read_from_snowflake():
        # TODO: create snowflake connector script 
        ...

    @abstractmethod
    def query_data():
        ...

    @abstractmethod 
    def format_for_folium():
        ... 

class WiFiData(BaseData):

    def __init__():
        self.path = Path("dataset/wifi_counts.csv")
        self.raw_df = None
        self.clean_df = None 


    def read_data(self):
        df = pd.read_csv(self.path)
        df.timestamp = pd.to_datetime(df.timestamp)
        self.raw_df = df.copy()
        del df 


    def query_data(self, date_str: str):
        # get dataframe subset for given data parameter 

        def validate_input(q: str):
            pattern = re.compile(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$') #validate string is in format yyyy-mm-dd
            result = re.match(pattern, q)
            if result is None:
                raise HTTPException(status_code=400, detail = "Invalid string format for date. Should be formatted as yyyy-mm-dd")
            else:
                ymd = [int(x) for x in q.split('-')]
                return datetime(year = ymd[0], month = ymd[1], day = ymd[2])
        

        date = validate_input(date_str)
        lower_bound = str(date)[:-9] #remove timestamp for query
        upper_bound = str(date + timedelta(1))[:-9] #remove timestamp for query
        query = f"timestamp >= '{lower_bound}' and timestamp < '{upper_bound}'"
            
        return df.query(query) 


    def __call__(self, date: datetime):
        # I am thinking we will make the instance callable so that data is initialized once but queries can be called during 
        # dependency injection 
        pass 


class DataFactory():
    # TODO: will revisit if this is needed in implementation
    pass
