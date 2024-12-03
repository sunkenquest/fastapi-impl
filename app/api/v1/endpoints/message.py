from fastapi import APIRouter, Depends, HTTPException
from app.schemas.message import SmsRequest
from app.services.message_service import send_message
from sqlalchemy.orm import Session

from app.db.connection import get_db


router = APIRouter()


@router.post("/")
def send_sms(request: SmsRequest, db: Session = Depends(get_db)):
    response = send_message(request.message, request.to, db)
    if response["status_code"] != 200:
        raise HTTPException(
            status_code=response["status_code"], detail=response["message"]
        )
    return response
