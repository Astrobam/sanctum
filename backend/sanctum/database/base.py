# backend/sanctum/database/base.py

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import text
from typing import Annotated
import uuid

# Define a custom type for UUID primary keys
uuid_pk = Annotated[
    uuid.UUID,
    mapped_column(primary_key=True, server_default=text("gen_random_uuid()")),
]

class Base(DeclarativeBase):
    """Base for all SQLAlchemy models."""
    pass
