# main.py

"""
    Start server by running the following command:
        uvicorn main:app
"""

from datetime import datetime 
from fastapi import Depends, FastAPI 
import pandas as pd 
from . import WiFiData

app = FastAPI()

# TODO
wifi_data = WiFiData() 



@app.get("/")
async def root():
    pass

# should these "get" or "post" methods? 
@app.get("/wifi/map")
async def generate_wifi_map(date: str =  Depends(wifi_data)): 
    '''
    Dependency Injection will automatically call the "callable" methods of the instance 
    which will create the subset of data for map and assign to a class variable. 
    Once the instance is in the path function scope. Another method will be called
    that will format data for folium and then pass to folium generation script

    Still need to determine how HTML should be returned. Could write locally to file (current set-up)
    or need to look into returning HTML from HTTP. (TODO) 
    '''
    pass 


@app.get("/bus/map")
async def generate_bus_map():
    pass


@app.get("/db")
async def test_db_query():
    # call db here
    pass 