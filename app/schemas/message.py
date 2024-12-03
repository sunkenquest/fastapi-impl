from pydantic import BaseModel, EmailStr


class SmsRequest(BaseModel):
    to: str
    message: str
