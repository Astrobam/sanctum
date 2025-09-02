# backend/sanctum/models/message.py

from sqlalchemy import String, func, TIMESTAMP, ForeignKey, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sanctum.database.base import Base, uuid_pk
from datetime import datetime
import uuid

class Message(Base):
    __tablename__ = "messages"

    message_id: Mapped[uuid_pk]
    conversation_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("conversations.conversation_id"), nullable=False)
    sender: Mapped[str] = mapped_column(String, nullable=False) # "user" or "ai"
    content: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )

    conversation: Mapped["Conversation"] = relationship(back_populates="messages")
