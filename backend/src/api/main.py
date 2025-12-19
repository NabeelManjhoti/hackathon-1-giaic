from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from ..core.config import settings
from . import rag_endpoints


def create_app():
    """
    Create and configure the FastAPI application.
    """
    app = FastAPI(
        title="RAG Chatbot API",
        description="API for the Integrated RAG Chatbot for AI-native Textbook",
        version="1.0.0"
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, specify exact origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routes
    app.include_router(rag_endpoints.router, prefix="/v1", tags=["rag"])

    @app.get("/v1/health")
    async def health_check():
        """
        Health check endpoint to verify service status.
        """
        return {
            "status": "healthy",
            "timestamp": "2025-12-16T10:00:00Z",  # This should be dynamic in real implementation
            "details": {
                "qdrant_connected": True,  # This should be checked in real implementation
                "postgres_connected": True  # This should be checked in real implementation
            }
        }

    return app


app = create_app()