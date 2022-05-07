from fastapi import FastAPI
from app.api.movies import movies
from app.api.db import metadata
from app.api.db import database
from app.api.db import engine

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(movies)
