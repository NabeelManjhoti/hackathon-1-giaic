# Quickstart Guide: Integrated RAG Chatbot

## Overview
This guide provides instructions for setting up and running the Integrated RAG Chatbot for AI-native Textbook project.

## Prerequisites
- Python 3.11+
- pip package manager
- Access to OpenAI API (with appropriate rate limits for free tier)
- Qdrant Cloud account (free tier)
- Neon Postgres account (free tier)

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-org/hackathon-1-giaic.git
cd hackathon-1-giaic
```

### 2. Set up Python Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r backend/requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the backend directory:
```env
OPENAI_API_KEY=your_openai_api_key
QDRANT_URL=your_qdrant_cluster_url
QDRANT_API_KEY=your_qdrant_api_key
DATABASE_URL=your_neon_postgres_connection_string
API_KEY=your_api_key_for_authentication
```

### 4. Install Dependencies
```bash
cd backend
pip install fastapi uvicorn openai qdrant-client python-dotenv pydantic sqlalchemy psycopg2-binary
```

## Running the Application

### 1. Start the FastAPI Server
```bash
cd backend
uvicorn src.main:app --reload --port 8000
```

### 2. Run Database Migrations (if applicable)
```bash
# If using Alembic for migrations
alembic upgrade head
```

### 3. Index Textbook Content
Run the ingestion script to index your textbook content into Qdrant:
```bash
python -m src.ingestion.index_textbook --file-path path/to/textbook.pdf
```

## API Usage

### Submit a Query
```bash
curl -X POST http://localhost:8000/v1/query \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your_api_key" \
  -d '{
    "query": "What is the principle of conservation of momentum?",
    "mode": "FULL_BOOK"
  }'
```

### Query with Selected Text
```bash
curl -X POST http://localhost:8000/v1/query \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your_api_key" \
  -d '{
    "query": "Explain this concept",
    "mode": "SELECTED_TEXT",
    "selected_text": "The principle of conservation of momentum states that in an isolated system..."
  }'
```

## Testing

### Run Unit Tests
```bash
cd backend
pytest tests/unit/ -v
```

### Run Integration Tests
```bash
cd backend
pytest tests/integration/ -v
```

## Deployment

### Deploy to Vercel (Backend API)
1. Install Vercel CLI: `npm i -g vercel`
2. Link your project: `vercel link`
3. Deploy: `vercel --prod`

### Environment Variables for Deployment
Set the same environment variables in your deployment platform:
- OPENAI_API_KEY
- QDRANT_URL
- QDRANT_API_KEY
- DATABASE_URL
- API_KEY

## Troubleshooting

### Common Issues
1. **Rate Limiting**: Ensure your API keys are within free-tier limits
2. **Qdrant Connection**: Verify your Qdrant URL and API key are correct
3. **Database Connection**: Check your Neon Postgres connection string

### Health Check
Check the service health at: `GET /v1/health`