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
from datetime import datetime 

import pandas as pd


#defining a Base Class since we have multiple data files 
class Data(ABC):

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

class WiFiData(Data):

    def __init__():
        self.path = Path("dataset/wifi_counts.csv")
        self.raw_df = None
        self.clean_df = None 


    def read_data(self):
        df = pd.read_csv(self.path)
        df.timestamp = pd.to_datetime(df.timestamp)
        self.raw_df = df.copy()
        del df 


    def query_data(self, date: datetime):
        pass


    def __call__(self, date: datetime):
        # I am thinking we will make the instance callable so that data is initialized once but queries can be called during 
        # dependency injection 
        pass 


class DataFactory():
    # TODO: will revisit if this is needed in implementation
    pass
