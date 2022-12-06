# main.py

"""
    Start server by running the following command:
        uvicorn main:app
"""

from datetime import datetime 
from pathlib import Path
import os

from fastapi import Depends, FastAPI 
from fastapi.responses import Response, HTMLResponse, FileResponse
import pandas as pd 

from data import WiFiData

#TODO: environment variables for paths 
#os.chdir( Path('/itsc4155-capstone-cyberninjas.github.io') )

app = FastAPI()

# TODO: once transit data is implemented, may need a factory
wifi_data = WiFiData().from_csv()


@app.get("/")
async def root():
    #TODO: look into using Jinja2 for handling HTML and returning through FastAPI 
    pass


@app.get("/wifi")
async def wifi():
    ''' base wifi page '''
    pass


@app.get("/wifi/map")
async def generate_wifi_map(date: str = Depends(wifi_data, use_cache=True)): 
    
    html_path = wifi_data.get_map().write_map()

    # Open html file and return 
    with open(html_path, 'r') as f:
        html_string = f.read()

    return HTMLResponse(content = html_string, status_code = 200)


@app.get("/wifi/data")
async def get_wifi_data(date: str = Depends(wifi_data, use_cache = True)):
    df = wifi_data.get_data()
    return Response(df.to_json(), media_type="application/json")


@app.get("/wifi/table")
async def get_wifi_table(date: str = Depends(wifi_data, use_cache = True)):
    df = wifi_data.get_data()
    return HTMLResponse(content=df.to_html(), status_code=200)


@app.get("/wifi/csv")
async def get_wifi_csv(date: str = Depends(wifi_data, use_cache = True)):
    file_path, name = wifi_data.write_csv()
    return FileResponse(path=file_path, filename=str(name))


@app.get("/transit/map")
async def generate_transit_map():
    #TODO: implement transit data class
    pass    

