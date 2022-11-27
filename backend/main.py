# main.py

"""
    Start server by running the following command:
        uvicorn main:app
"""

from datetime import datetime 

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    pass

# should these "get" or "post" methods? The end points are 
@app.post("/wifi/map")
async def generate_wifi_map(date: datetime): # TODO: Python Datetime supported 
    return {'date': date}

@app.get("/bus/map")
async def generate_bus_map():
    pass

@app.get("/db")
async def test_db_query():
    # call db here
    pass 