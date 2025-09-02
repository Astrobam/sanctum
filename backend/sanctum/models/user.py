# backend/sanctum/models/user.py

from sqlalchemy import String, func, TIMESTAMP, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sanctum.database.base import Base, uuid_pk
from datetime import datetime
from typing import List

class User(Base):
    __tablename__ = "users"

    user_id: Mapped[uuid_pk]
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )

    conversations: Mapped[List["Conversation"]] = relationship(back_populates="user")
