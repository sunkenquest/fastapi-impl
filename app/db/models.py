from sqlalchemy import Column, Integer, String, Text
from .connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    message_body = Column(Text, nullable=False)
    recipient = Column(String, nullable=False)
    message_sid = Column(String, nullable=True)
