# backend/sanctum/schemas/message.py

from pydantic import BaseModel
from datetime import datetime
import uuid

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    message_id: uuid.UUID
    conversation_id: uuid.UUID
    sender: str
    timestamp: datetime

    class Config:
        from_attributes = True
