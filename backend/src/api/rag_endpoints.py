from fastapi import APIRouter, Depends, HTTPException, status, Request
from typing import Optional
from pydantic import BaseModel
import uuid
from ..models.query import QueryModel, QueryMode
from ..models.response import ResponseModel
from ..services.rag_service import RAGService
from ..core.vector_store import VectorStore
from ..services.embedding_service import EmbeddingService
from ..middleware.rate_limit import check_rate_limit
from ..core.config import settings
from ..core.logging import log_request, log_response, log_error


router = APIRouter()


def verify_api_key(request: Request) -> str:
    """
    Verify the API key from the request headers.
    """
    api_key = request.headers.get("X-API-Key")
    if not api_key or api_key != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    return api_key


# Request/Response models for API
class QueryRequest(BaseModel):
    query: str
    mode: QueryMode
    selected_text: Optional[str] = None
    include_references: bool = True


class QueryResponse(BaseModel):
    response: str
    references: list
    query_id: str
    confidence_score: Optional[float] = None


@router.post("/query", response_model=QueryResponse)
async def full_book_query(
    request: QueryRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Submit a query to the RAG chatbot for the full-book mode.
    """
    # Check rate limit using the API key as identifier
    await check_rate_limit(api_key)

    # Log the incoming request
    log_request("anonymous", request.query, request.mode.value)

    # Create query model
    query_model = QueryModel(
        text=request.query,
        mode=request.mode,
        selected_text=request.selected_text
    )

    # Initialize services
    vector_store = VectorStore()
    embedding_service = EmbeddingService()
    rag_service = RAGService(vector_store, embedding_service)

    try:
        # Process the query
        response = await rag_service.process_query(query_model)

        # Format the response
        formatted_response = QueryResponse(
            response=response.content,
            references=[
                {
                    "source": ref.source,
                    "page_number": ref.page_number,
                    "section": ref.section,
                    "text_preview": ref.text_preview
                }
                for ref in response.references
            ],
            query_id=response.query_id,
            confidence_score=response.confidence_score
        )

        # Log the response
        log_response("anonymous", response.query_id, response.content, response.confidence_score or 0.0)

        return formatted_response
    except Exception as e:
        # Log the error
        log_error(e, f"Processing query from API key {api_key}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your query"
        )
    finally:
        # Ensure resources are closed
        vector_store.close()


@router.post("/query/stream")
async def stream_query(
    request: QueryRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Submit a query with streaming response.
    """
    # For now, return the same as the regular query endpoint
    # In a real implementation, this would return a streaming response
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Streaming response not yet implemented"
    )


@router.post("/query/selected-text", response_model=QueryResponse)
async def selected_text_query(
    request: QueryRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Submit a query to the RAG chatbot for the selected-text mode.
    This endpoint processes queries that are constrained to specific user-selected text.
    """
    # Check rate limit using the API key as identifier
    await check_rate_limit(api_key)

    # Validate that this is a selected-text query
    if request.mode != QueryMode.SELECTED_TEXT:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This endpoint only accepts SELECTED_TEXT mode queries"
        )

    # Validate that selected_text is provided
    if not request.selected_text or len(request.selected_text.strip()) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Selected text is required for selected-text mode queries"
        )

    # Log the incoming request
    log_request("anonymous", request.query, request.mode.value)

    # Create query model
    query_model = QueryModel(
        text=request.query,
        mode=request.mode,
        selected_text=request.selected_text
    )

    # Initialize services
    vector_store = VectorStore()
    embedding_service = EmbeddingService()
    rag_service = RAGService(vector_store, embedding_service)

    try:
        # Process the query
        response = await rag_service.process_query(query_model)

        # Format the response
        formatted_response = QueryResponse(
            response=response.content,
            references=[
                {
                    "source": ref.source,
                    "page_number": ref.page_number,
                    "section": ref.section,
                    "text_preview": ref.text_preview
                }
                for ref in response.references
            ],
            query_id=response.query_id,
            confidence_score=response.confidence_score
        )

        # Log the response
        log_response("anonymous", response.query_id, response.content, response.confidence_score or 0.0)

        return formatted_response
    except Exception as e:
        # Log the error
        log_error(e, f"Processing selected-text query from API key {api_key}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your selected-text query"
        )
    finally:
        # Ensure resources are closed
        vector_store.close()