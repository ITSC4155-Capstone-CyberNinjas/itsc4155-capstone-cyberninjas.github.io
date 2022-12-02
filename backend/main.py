# main.py

"""
    Start server by running the following command:
        uvicorn main:app
"""

from datetime import datetime 
from fastapi import Depends, FastAPI 
import pandas as pd 

app = FastAPI()

# call data class

@app.get("/")
async def root():
    pass

# should these "get" or "post" methods? The end points are 
@app.get("/wifi/map")
async def generate_wifi_map(date: str): # TODO: Python Datetime supported 
    df = pd.DataFrame()
    print('hi')
    return {'date': date}

@app.get("/bus/map")
async def generate_bus_map():
    pass

@app.get("/db")
async def test_db_query():
    # call db here
    pass 