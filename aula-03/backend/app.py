from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

psytrance_artists = [
    "Infected Mushroom",
    "Astrix",
    "Vini Vici",
    "Skazi",
    "Talamasca",
    "Raja Ram",
    "Sesto Sento",
    "Captain Hook",
    "Ace Ventura",
    "Bizarre Contact"
]

class ArtistResponse(BaseModel):
    artists: List[str]

API_VERSION = "1.0.0"

@app.get("/version")
async def get_version():
    return {"version": API_VERSION}

@app.get("/list", response_model=ArtistResponse)
async def get_artists():
    return {"artists": psytrance_artists}