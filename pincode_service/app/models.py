# coding: utf-8
from sqlalchemy import ARRAY
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Pincode(Base):
    __tablename__ = "pincode"

    officename = Column(String, primary_key=True, nullable=False)
    pincode = Column(Integer, primary_key=True, nullable=False)
    officetype = Column(String)
    deliverystatus = Column(String, primary_key=True, nullable=False)
    divisionname = Column(String)
    regionname = Column(String)
    circlename = Column(String)
    taluk = Column(String, primary_key=True, nullable=False)
    districtname = Column(String, primary_key=True, nullable=False)
    statename = Column(String)
    telephone = Column(String, primary_key=True, nullable=False)
    relatedsuboffice = Column(String)
    relatedheadoffice = Column(String)
    longitude = Column(Float(53))
    latitude = Column(Float(53))
