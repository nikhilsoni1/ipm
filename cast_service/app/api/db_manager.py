from app.api.models import CastOut
from app.api.models import CastIn
from app.api.models import CastUpdate
from app.api.db import casts
from app.api.db import database


async def add_cast(payload: CastIn):
    query = casts.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_cast(id):
    query = casts.select(casts.c.id == id)
    return await database.fetch_one(query=query)
