from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.connection import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, find_user

router = APIRouter()


@router.post("/", response_model=UserResponse)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = find_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
