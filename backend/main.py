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

os.chdir( Path('/home/calvin/capstone/itsc4155-capstone-cyberninjas.github.io') )

app = FastAPI()

# TODO
wifi_data = WiFiData().from_csv()



@app.get("/")
async def root():
    #TODO: look into using Jinja2 for handling HTML and returning through FastAPI 

    html_content = """
    """
    return HTMLResponse(content=html_content, status_code=200)

# should these "get" or "post" methods? 
@app.get("/wifi/map")
async def generate_wifi_map(date: str = Depends(wifi_data, use_cache=True)): 
    '''
    Dependency Injection will automatically call the "callable" methods of the instance 
    which will create the subset of data for map and assign to a class variable. 
    Once the instance is in the path function scope. Another method will be called
    that will format data for folium and then pass to folium generation script

    Still need to determine how HTML should be returned. Could write locally to file (current set-up)
    or need to look into returning HTML from HTTP. (TODO) 
    '''

    wifi_map = wifi_data.get_map()
    html_path = wifi_map.write_map()

    with open(html_path, 'r') as f:
        html_string = f.read()

    return HTMLResponse(content = html_string, status_code = 200)


@app.get("/bus/map")
async def generate_bus_map():
    directory = os.getcwd()
    return {"pwd": directory}


@app.get("/db")
async def test_db_query():
    # call db here
    pass 