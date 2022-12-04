# main.py

"""
    Start server by running the following command:
        uvicorn main:app
"""

from datetime import datetime 
from pathlib import Path
import os

from fastapi import Depends, FastAPI 
from fastapi.responses import HTMLResponse
import pandas as pd 

from data import WiFiData

#TODO: environment variables for paths 
os.chdir( Path('/home/calvin/capstone/itsc4155-capstone-cyberninjas.github.io') )

app = FastAPI()

# TODO: once transit data is implemented, may need a factory
wifi_data = WiFiData().from_csv()


@app.get("/")
async def root():
    #TODO: look into using Jinja2 for handling HTML and returning through FastAPI 
    pass


@app.get("/wifi/map")
async def generate_wifi_map(date: str = Depends(wifi_data, use_cache=True)): 
    '''
    Return HTML for wifi traffic heatmap

    Params:
        date (str): 
            String representation of date of interest (yyyy-mm-dd)

    Dependencies:
        wifi_data (WifiData): 
            Data class for handling queries and operations of wifi data. The "date" 
            query parameter is passed to the instance to initiate query

    Returns:
        HTMLResponse: Raw HTML for Heatmap 

    '''

    wifi_map = wifi_data.get_map()
    html_path = wifi_map.write_map()

    with open(html_path, 'r') as f:
        html_string = f.read()

    return HTMLResponse(content = html_string, status_code = 200)


@app.get("/transit/map")
async def generate_bus_map():
    #TODO: implement transit data class
    pass

