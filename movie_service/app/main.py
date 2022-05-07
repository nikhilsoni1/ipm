from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List
from pprint import pprint

app = FastAPI()

fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order once again.',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]

class Movie(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]


# @app.get('/', response_model=List[Movie])
# async def index():
#     return fake_movie_db

@app.post('/', status_code=201)
async def add_movie(payload: Movie):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {'id': len(fake_movie_db) - 1}

@app.put('/{id}')
async def update_movie(id: int, payload: Movie):
    movie = payload.dict()
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        fake_movie_db[id] = movie
        return None
    raise HTTPException(status_code=404, detail=f"Movie with given {id} (ID) not found")