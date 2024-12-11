from pydantic import BaseModel


class SmsRequest(BaseModel):
    to: str
    message: str
