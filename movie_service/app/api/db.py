# This file interfaces with the database
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy import ARRAY
from databases import Database
import os

DATABASE_URI = os.getenv("DATABASE_URI")
engine = create_engine(DATABASE_URI)
metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("plot", String(250)),
    Column("genres", ARRAY(String)),
    Column("casts", ARRAY(Integer)),
)

database = Database(DATABASE_URI)
