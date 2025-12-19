# API Reference: RAG Chatbot

## Overview

The RAG Chatbot API provides endpoints for querying textbook content with evidence-based responses. The API supports both full-book queries and selected-text queries.

## Authentication

All API requests require an API key in the `X-API-Key` header:

```
X-API-Key: your_api_key_here
```

## Endpoints

### Query Textbook Content

`POST /v1/query`

Submit a query to the RAG chatbot.

#### Request Body

```json
{
  "query": "Your question here",
  "mode": "FULL_BOOK",
  "selected_text": "Optional text for SELECTED_TEXT mode",
  "include_references": true
}
```

#### Path Parameters

- `mode`: Either "FULL_BOOK" or "SELECTED_TEXT"

#### Response

```json
{
  "response": "The answer to your query",
  "references": [
    {
      "source": "textbook",
      "page_number": 42,
      "section": "Chapter 3: Physics",
      "text_preview": "The relevant text..."
    }
  ],
  "query_id": "unique-query-id",
  "confidence_score": 0.85
}
```

### Query with Selected Text

`POST /v1/query/selected-text`

Submit a query constrained to user-selected text.

#### Request Body

```json
{
  "query": "Your question about the selected text",
  "mode": "SELECTED_TEXT",
  "selected_text": "The text you want to focus on",
  "include_references": true
}
```

### Health Check

`GET /v1/health`

Check the health status of the service.

#### Response

```json
{
  "status": "healthy",
  "timestamp": "2025-12-16T10:00:00Z",
  "details": {
    "qdrant_connected": true,
    "postgres_connected": true
  }
}
```

## Rate Limiting

The API implements rate limiting to comply with free-tier constraints. Requests are limited to 100 per hour per API key.

## Error Responses

The API returns standard HTTP error codes:

- `400`: Bad request (invalid parameters)
- `401`: Unauthorized (invalid API key)
- `429`: Rate limit exceeded
- `500`: Internal server error