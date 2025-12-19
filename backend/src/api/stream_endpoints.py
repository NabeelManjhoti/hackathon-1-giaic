from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator
import json
from ..models.query import QueryMode
from ..services.rag_service import RAGService
from ..core.vector_store import VectorStore
from ..services.embedding_service import EmbeddingService
from ..services.chat_service import ChatService
from ..core.chat_config import ChatConfig
from ..middleware.rate_limit import check_rate_limit
from ..core.config import settings
from ..core.logging import log_request, log_error


router = APIRouter()


async def event_generator(query: str, mode: QueryMode, selected_text: str = None, api_key: str = None):
    """
    Generator that yields streaming events for the chat response.
    """
    try:
        # Initialize services
        vector_store = VectorStore()
        embedding_service = EmbeddingService()
        rag_service = RAGService(vector_store, embedding_service)
        chat_service = ChatService(ChatConfig.get_default_config())

        # Create query model
        from ..models.query import QueryModel
        query_model = QueryModel(
            text=query,
            mode=mode,
            selected_text=selected_text
        )

        # Process the query to get relevant chunks
        response = await rag_service.process_query(query_model)

        # Prepare messages for chat
        messages = [
            {"role": "user", "content": query}
        ]

        # Generate streaming response
        async for token in chat_service.generate_response_stream(
            messages,
            [{"content": ref.text_preview, "metadata": {"section": ref.section, "page_number": ref.page_number}}
             for ref in response.references]
        ):
            yield f"data: {json.dumps({'token': token})}\n\n"

    except Exception as e:
        log_error(e, f"Streaming response error for API key {api_key}")
        yield f"data: {json.dumps({'error': 'An error occurred during streaming'})}\n\n"
    finally:
        # Ensure resources are closed
        if 'vector_store' in locals():
            vector_store.close()


@router.post("/stream-query")
async def stream_query_endpoint(
    request: Request,
    api_key: str = Depends(verify_api_key)
):
    """
    Stream a query response using Server-Sent Events.
    """
    # Check rate limit using the API key as identifier
    await check_rate_limit(api_key)

    # Parse request body
    body = await request.json()
    query = body.get("query", "")
    mode_str = body.get("mode", "FULL_BOOK")
    selected_text = body.get("selected_text", None)

    # Validate mode
    try:
        mode = QueryMode(mode_str)
    except ValueError:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="Invalid query mode")

    # Log the incoming request
    log_request("anonymous", query, mode_str)

    # Create streaming response
    return StreamingResponse(
        event_generator(query, mode, selected_text, api_key),
        media_type="text/event-stream"
    )


def verify_api_key(request: Request) -> str:
    """
    Verify the API key from the request headers.
    """
    api_key = request.headers.get("X-API-Key")
    if not api_key or api_key != settings.api_key:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    return api_key