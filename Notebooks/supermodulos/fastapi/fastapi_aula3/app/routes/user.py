from fastapi import APIRouter, Depends
from app.schemas.user import User
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.user import create_user, get_users
from typing import List


router = APIRouter()


def get_db():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()


@router.post('/usuario', response_model=User, status_code=201)
def create_user_route(user: User, db: Session = Depends(get_db)):
    return create_user(user=user, db=db)


@router.get('/usuarios', response_model=List[User])
def list_users(db: Session = Depends(get_db)):
    return get_users(db=db)
