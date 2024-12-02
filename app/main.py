from fastapi import FastAPI
from app.db.connection import engine, Base
from app.api.v1.endpoints import users, message

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(message.router, prefix="/api/v1/sms", tags=["Message"])
