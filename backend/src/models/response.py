from pydantic import BaseModel, Field, validator
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime


class Reference(BaseModel):
    source: str
    page_number: int
    section: str
    text_preview: Optional[str] = None


class ResponseModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    query_id: str
    content: str
    references: List[Reference] = []
    confidence_score: Optional[float] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    @validator('confidence_score')
    def validate_confidence_score(cls, v):
        if v is not None and (v < 0.0 or v > 1.0):
            raise ValueError('Confidence score must be between 0.0 and 1.0')
        return v

    @validator('references')
    def validate_references(cls, v):
        if len(v) == 0:
            raise ValueError('Response must cite at least one textbook content chunk')
        return v