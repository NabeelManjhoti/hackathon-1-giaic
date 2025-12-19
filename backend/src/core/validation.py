from typing import Optional
from fastapi import HTTPException, status
from pydantic import BaseModel, validator
from ..models.query import QueryModel


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def validate_query_request(query: str, mode: str, selected_text: Optional[str] = None) -> bool:
    """
    Validate the query request parameters.

    Args:
        query: The query text
        mode: The query mode (FULL_BOOK or SELECTED_TEXT)
        selected_text: Optional selected text for SELECTED_TEXT mode

    Returns:
        True if valid, raises ValidationError if not
    """
    # Validate query length
    if not query or len(query.strip()) < 10:
        raise ValidationError("Query must be at least 10 characters long")

    if len(query) > 1000:
        raise ValidationError("Query must be no more than 1000 characters long")

    # Validate mode
    if mode not in ["FULL_BOOK", "SELECTED_TEXT"]:
        raise ValidationError("Mode must be either FULL_BOOK or SELECTED_TEXT")

    # If mode is SELECTED_TEXT, selected_text must be provided and not empty
    if mode == "SELECTED_TEXT" and (not selected_text or len(selected_text.strip()) == 0):
        raise ValidationError("Selected text is required for SELECTED_TEXT mode")

    return True


def handle_validation_error(error: ValidationError) -> HTTPException:
    """
    Convert a validation error to an HTTP exception.

    Args:
        error: The validation error

    Returns:
        HTTPException with appropriate status code and message
    """
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=str(error)
    )