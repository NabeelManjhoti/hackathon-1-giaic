from pydantic import BaseModel, Field, validator
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum


class QueryMode(str, Enum):
    FULL_BOOK = "FULL_BOOK"
    SELECTED_TEXT = "SELECTED_TEXT"


class QueryStatus(str, Enum):
    CREATED = "CREATED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"


class QueryModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    text: str
    mode: QueryMode
    selected_text: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    session_id: Optional[str] = None
    status: QueryStatus = QueryStatus.CREATED

    @validator('text')
    def validate_text_length(cls, v):
        if len(v) < 10 or len(v) > 1000:
            raise ValueError('Query text must be between 10 and 1000 characters')
        return v

    @validator('mode')
    def validate_mode(cls, v):
        if v not in [QueryMode.FULL_BOOK, QueryMode.SELECTED_TEXT]:
            raise ValueError('Mode must be either FULL_BOOK or SELECTED_TEXT')
        return v