from numpy import integer
from pydantic import BaseModel
from typing import List
from typing import Optional


class Pincode(BaseModel):
    officename: str
    pincode: int
    officetype: str
    deliverystatus: str
    divisionname: str
    regionname: str
    circlename: str
    taluk: str
    districtname: str
    statename: str
    telephone: str
    relatedsuboffice: str
    relatedheadoffice: str
    longitude: float
    latitude: float
