from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import User as UserSchema


def create_user(db: Session, user: UserSchema):
    db_user = UserModel(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(UserModel).all()
