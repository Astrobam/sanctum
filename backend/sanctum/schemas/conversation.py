# backend/sanctum/schemas/conversation.py

from pydantic import BaseModel
from datetime import datetime
from typing import List
import uuid

from .message import Message

class ConversationBase(BaseModel):
    persona: str

class ConversationCreate(ConversationBase):
    pass

class Conversation(ConversationBase):
    conversation_id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime
    messages: List[Message] = []

    class Config:
        from_attributes = True
