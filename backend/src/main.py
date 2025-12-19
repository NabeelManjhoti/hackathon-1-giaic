"""
Main entry point for the RAG Chatbot API.
"""
from .api.main import app

# This file serves as the entry point for the application
# When running with uvicorn, use: uvicorn src.main:app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)