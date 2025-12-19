from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime


class QueryMode(str, Enum):
    FULL_BOOK = "FULL_BOOK"
    SELECTED_TEXT = "SELECTED_TEXT"


class QueryRequest(BaseModel):
    query: str
    mode: QueryMode
    selected_text: Optional[str] = None
    include_references: bool = True


class Reference(BaseModel):
    source: str
    page_number: int
    section: str
    text_preview: Optional[str] = None


class QueryResponse(BaseModel):
    response: str
    references: List[Reference]
    query_id: str
    confidence_score: Optional[float] = None


class HealthResponse(BaseModel):
    status: str
    timestamp: str
    details: Optional[Dict[str, Any]] = None


class TextbookChunk(BaseModel):
    chunk_id: str
    content: str
    metadata: Dict[str, Any]
    embedding: Optional[List[float]] = None
    source_reference: str