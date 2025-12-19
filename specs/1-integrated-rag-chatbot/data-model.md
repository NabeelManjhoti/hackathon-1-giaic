# Data Model: Integrated RAG Chatbot

## Entities

### Query
- **Description**: A question or request for information from the textbook
- **Fields**:
  - `id`: UUID (primary key)
  - `text`: String (the actual question text)
  - `mode`: Enum (FULL_BOOK or SELECTED_TEXT)
  - `selected_text`: String (optional, for selected-text mode)
  - `timestamp`: DateTime (when the query was made)
  - `session_id`: String (optional, for tracking without persistence)

### TextbookContent
- **Description**: Pre-indexed chunks of the textbook stored in Qdrant
- **Fields**:
  - `chunk_id`: String (unique identifier for the chunk)
  - `content`: String (the actual text content of the chunk)
  - `metadata`: JSON (book section, page number, chapter, etc.)
  - `embedding`: Vector (the vector representation for similarity search)
  - `source_reference`: String (reference to the original location in the textbook)

### Response
- **Description**: Answer to the user's query with evidence references
- **Fields**:
  - `id`: UUID (primary key)
  - `query_id`: UUID (foreign key to Query)
  - `content`: String (the answer text)
  - `references`: Array of String (references to textbook sections/chunks)
  - `confidence_score`: Float (confidence level of the response)
  - `timestamp`: DateTime (when the response was generated)

### UserSelection
- **Description**: Highlighted text in the textbook that constrains the scope of the query
- **Fields**:
  - `id`: UUID (primary key)
  - `text`: String (the selected text)
  - `context_before`: String (text before selection for context)
  - `context_after`: String (text after selection for context)
  - `source_location`: String (where in the textbook this was selected from)

## Relationships
- Query may have one Response (1:1)
- Response references multiple TextbookContent chunks (1:many)
- Query may have one UserSelection (1:1, optional)

## Validation Rules
- Query.text must be between 10 and 1000 characters
- Query.mode must be either FULL_BOOK or SELECTED_TEXT
- Response.content must cite at least one TextbookContent chunk
- TextbookContent.chunk_id must be unique
- Confidence score must be between 0.0 and 1.0

## State Transitions
- Query: CREATED → PROCESSING → COMPLETED
- Response: GENERATING → VALIDATED → DELIVERED