from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists.",
        )

    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def find_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
