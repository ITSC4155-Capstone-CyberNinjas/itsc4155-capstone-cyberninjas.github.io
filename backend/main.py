# main.py

"""
    Start server by running the following command:
        uvicorn main:app
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/map")
async def test():
    return {"message": "Test returned"}