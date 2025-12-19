# Research: Integrated RAG Chatbot Implementation

## Decision: Embedding Model Selection
**Rationale**: OpenAI text-embedding-3-small offers the best balance of cost and performance for the hackathon project with free-tier constraints. While the "large" model might provide slightly better accuracy, the cost difference is significant and the "small" model still provides excellent performance for textbook content retrieval.
**Alternatives considered**:
- text-embedding-3-large (higher accuracy, higher cost)
- Open-source alternatives like Sentence Transformers (free but requires more computational resources)
- Cohere embeddings (different pricing model)

## Decision: Top-k Retrieval Value
**Rationale**: Using top-k=5 as determined in the clarification session, with initial retrieval of 10 items and reranking to select the top 5. This provides good balance between retrieval quality and system performance.
**Alternatives considered**:
- Lower k values (3) - potentially miss relevant content
- Higher k values (10+) - increased computational cost and context length

## Decision: Reranking Implementation
**Rationale**: Yes, implement reranking using cross-encoder models to improve the relevance of retrieved chunks. This will enhance the quality of responses by ensuring the most contextually relevant chunks are used.
**Alternatives considered**:
- No reranking - simpler but potentially lower quality results
- Lexical reranking - less effective for semantic similarity

## Decision: Chat History Storage
**Rationale**: Stateless design as determined in clarification - no chat history storage. Each query is independent to comply with the constraint of no user authentication or personalization.
**Alternatives considered**:
- Postgres sessions (violates no-auth constraint)
- In-memory storage (violates stateless requirement)

## Decision: Selected-text Handling Method
**Rationale**: Direct injection of selected text into the RAG pipeline with mode flag to distinguish between full-book and selected-text queries. This allows the system to constrain responses to only the selected content.
**Alternatives considered**:
- Passage ID approach (requires additional indexing of selected text)
- Separate index for selected text (complexity overhead)

## Decision: Architecture Components
**Rationale**: System architecture will include:
- Data ingestion service for textbook content
- Vector indexing pipeline using Qdrant
- FastAPI backend with OpenAI integration
- ChatKit SDK for conversation handling
- Integration endpoints for frontend communication
**Alternatives considered**: Various architectural patterns but selected microservice approach for clarity and separation of concerns.

## Decision: Testing Strategy
**Rationale**: Comprehensive testing approach including:
- Unit tests for retrieval relevance using mock Qdrant
- Integration tests for full-book vs selected-text modes
- Manual validation against acceptance criteria
- Performance testing to ensure low-latency responses
**Alternatives considered**: Different testing frameworks and methodologies but selected standard Python testing approaches.