# backend/sanctum/routers/conversations.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from sanctum import schemas, models
from sanctum.routers.auth import get_db
from sanctum.routers.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Conversation, status_code=status.HTTP_201_CREATED)
def create_conversation(
    conversation: schemas.ConversationCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    db_conversation = models.Conversation(
        **conversation.model_dump(), user_id=current_user.user_id
    )
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation


@router.get("/", response_model=List[schemas.Conversation])
def read_conversations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    conversations = (
        db.query(models.Conversation)
        .filter(models.Conversation.user_id == current_user.user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return conversations


@router.post("/{conversation_id}/messages", response_model=schemas.Message)
def create_message_for_conversation(
    conversation_id: str,
    message: schemas.MessageCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    # For now, we are not connecting to the AI core.
    # We will just save the user's message.
    db_message = models.Message(
        **message.model_dump(),
        conversation_id=conversation_id,
        sender="user"
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
