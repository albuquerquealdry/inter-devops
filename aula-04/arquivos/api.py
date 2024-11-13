from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

origins = [
    "http://localhost",  
    "http://127.0.0.1",  
    "http://localhost:8000",  
    "http://127.0.0.1:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class Artist(BaseModel):
    name: str
    country: str

artists = [
    {"name": "Astrix", "country": "Israel"},
    {"name": "Ace Ventura", "country": "Israel"},
    {"name": "Liquid Soul", "country": "Suíça"},
    {"name": "Infected Mushroom", "country": "Israel"},
    {"name": "Ajja", "country": "Suíça"},
    {"name": "Dekel", "country": "Israel"},
    {"name": "Morten Granau", "country": "Dinamarca"}  
]

@app.get("/artists", response_model=List[Artist])
async def get_artists():
    return [Artist(**artist) for artist in artists]
