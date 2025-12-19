from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4


class UserSelectionModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    text: str
    context_before: Optional[str] = None
    context_after: Optional[str] = None
    source_location: Optional[str] = None