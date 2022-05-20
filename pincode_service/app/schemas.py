from typing import Union
from typing import List
from pydantic import BaseModel


class Pincode(BaseModel):
    officename: str
    pincode: int
    officetype: Union[str, None]
    deliverystatus: str
    divisionname: Union[str, None]
    regionname: Union[str, None]
    circlename: Union[str, None]
    taluk: str
    districtname: str
    statename: Union[str, None]
    telephone: str
    relatedsuboffice: Union[str, None]
    relatedheadoffice: Union[str, None]
    longitude: Union[float, None]
    latitude: Union[float, None]

    class Config:
        orm_mode = True

class GetPincode(Pincode):
    pincodes: List[Pincode]
