import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from twilio.rest import Client
from app.db.models import Message


load_dotenv()

account_sid = os.getenv("TWILIO_ACC_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")


def send_message(message, to, db: Session):
    try:
        client = Client(account_sid, auth_token)

        sms = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=to,
        )

        message_record = Message(
            message_body=message, recipient=to, message_sid=sms.sid
        )
        db.add(message_record)
        db.commit()

        return {
            "message": f"Message sent successfully: {sms.sid}",
            "status_code": 200,
        }
    except Exception as e:
        return {
            "message": f"Failed to send message: {str(e)}",
            "status_code": 400,
        }
