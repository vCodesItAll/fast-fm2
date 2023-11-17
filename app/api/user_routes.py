from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, controllers
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return controllers.create_user(db=db, user=user)
