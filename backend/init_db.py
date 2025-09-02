# backend/init_db.py

import logging
from sanctum.database.session import engine
from sanctum.database.base import Base
# Import all models to ensure they are registered with SQLAlchemy's metadata
from sanctum.models.user import User
from sanctum.models.conversation import Conversation
from sanctum.models.message import Message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    logger.info("Creating all database tables...")
    # The Base object has a metadata attribute that stores all the table definitions.
    # create_all checks for the existence of tables before creating them.
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully.")

if __name__ == "__main__":
    init_db()
