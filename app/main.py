from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal
from database import engine


title = "API for Indian Pincodes"
app = FastAPI(title=title)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(path="/{pincode}", response_model=schemas.Pincode)
def get_pincode(pincode: int, db: Session = Depends(get_db)):
    result = crud.get_pincode(db, pincode=pincode)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result
