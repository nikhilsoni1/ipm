from sqlalchemy.orm import Session
import models
import schemas

def get_pincode(db: Session, pincode: int):
    result = db.query(models.Pincode).filter(models.Pincode.pincode == pincode).first()
    return result