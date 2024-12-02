import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from twilio.rest import Client
from app.schemas.message import SmsRequest


router = APIRouter()

load_dotenv()

account_sid = os.getenv("TWILIO_ACC_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")


@router.post("/")
def send_sms(request: SmsRequest):
    try:
        client = Client(account_sid, auth_token)
        sms = client.messages.create(
            body=request.message,
            from_=twilio_phone_number,
            to=request.to,
        )
        return {"message": f"Message sent successfully: {sms.sid}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to send message: {str(e)}")
