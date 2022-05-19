from typing import List
from fastapi import APIRouter
from fastapi import HTTPException
from app.api.models import Pincode
from app.api import db_manager

pincode = APIRouter()


@pincode.get("/{pincode}/", response_model=List[Pincode])
async def get_pincode():
    return await db_manager.get_all_movies()
