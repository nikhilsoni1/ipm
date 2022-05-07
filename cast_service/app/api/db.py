import os
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy import ARRAY
from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

casts = Table(
    "casts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("nationality", String(20)),
)

database = Database(DATABASE_URI)
