from fastapi import APIRouter, HTTPException
from app.schemas.message import SmsRequest
from app.services.message_service import send_message

router = APIRouter()


@router.post("/")
def send_sms(request: SmsRequest):
    response = send_message(request.message, request.to)
    if response["status_code"] != 200:
        raise HTTPException(
            status_code=response["status_code"], detail=response["message"]
        )
    return response
