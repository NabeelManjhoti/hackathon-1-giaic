# RAG Chatbot Backend

This is the backend service for the Integrated RAG Chatbot for AI-native Textbook project.

## Overview

The backend provides a RAG (Retrieval-Augmented Generation) system that allows students to ask questions about textbook content and receive accurate, context-aware responses with evidence references.

## Features

- Full-book RAG queries
- Selected-text constrained queries
- Evidence-based responses with references
- Vector search using Qdrant
- OpenAI integration for response generation
- Rate limiting for free-tier compliance

## Tech Stack

- Python 3.11
- FastAPI
- OpenAI API
- Qdrant Vector Store
- Pydantic for data validation

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   # Create .env file with the following variables:
   OPENAI_API_KEY=your_openai_api_key
   QDRANT_URL=your_qdrant_cluster_url
   QDRANT_API_KEY=your_qdrant_api_key
   DATABASE_URL=your_neon_postgres_connection_string
   API_KEY=your_api_key_for_authentication
   ```

3. Run the application:
   ```bash
   uvicorn src.api.main:app --reload --port 8000
   ```

## API Endpoints

- `POST /v1/query` - Submit a query to the RAG system
- `POST /v1/query/selected-text` - Submit a query with selected text context
- `GET /v1/health` - Health check endpoint

## Ingestion

To ingest textbook content:

```bash
python -m src.cli.ingest --file-path path/to/textbook.txt --title "Textbook Title"
```

## Environment Variables

- `OPENAI_API_KEY` - OpenAI API key
- `QDRANT_URL` - Qdrant cluster URL
- `QDRANT_API_KEY` - Qdrant API key
- `DATABASE_URL` - Database connection string
- `API_KEY` - API key for authentication