# Feature Specification: Integrated RAG Chatbot for AI-native Textbook

**Feature Branch**: `1-integrated-rag-chatbot`
**Created**: 2025-12-16
**Status**: Draft
**Input**: User description: "Project: Integrated RAG Chatbot for AI-native Textbook (Physical AI & Humanoid Robotics)
Target audience: Students and learners interacting with the published book
Focus: Accurate, context-aware assistance on textbook content
Success criteria:
- Answers general questions using full-book retrieval from Qdrant
- Correctly answers questions restricted to user-selected text only
- Provides evidence-based responses with references to relevant sections/chunks
- Enhances interactive learning (hackathon bonus)
Constraints:
- Tech stack: OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres, Qdrant Cloud Free Tier
- Seamless integration with frontend at hackathon-1-giaic.vercel.app
- Free-tier limits only
- Deployment-ready by hackathon deadline
Not building:
- General-purpose AI chatbot (no external knowledge)
- Multi-modal features (images, code execution)
- User authentication or long-term personalization
- Advanced agent tools beyond basic RAG"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Full-book RAG Query (Priority: P1)

Student asks general questions about the textbook content and receives accurate, context-aware responses based on the entire book.

**Why this priority**: This is the core functionality that provides value to students by enabling them to get answers from the entire textbook content.

**Independent Test**: Can be fully tested by submitting questions to the chatbot and verifying that responses are accurate and sourced from the textbook content in Qdrant.

**Acceptance Scenarios**:
1. **Given** a student has access to the textbook chatbot interface, **When** they ask a general question about the textbook content, **Then** the chatbot returns an accurate answer with references to relevant sections from the full book.
2. **Given** a student asks a question requiring information from multiple parts of the book, **When** they submit the question, **Then** the chatbot synthesizes information from relevant sections and provides a comprehensive response.

---

### User Story 2 - User-selected Text Query (Priority: P2)

Student highlights specific text in the textbook and asks questions only about that selected text, receiving responses constrained to the selected content.

**Why this priority**: This provides a focused learning mode that allows students to get specific clarifications on text they're currently reading.

**Independent Test**: Can be tested by selecting specific text portions and verifying that responses are restricted to information within the selected text only.

**Acceptance Scenarios**:
1. **Given** a student has selected specific text in the textbook interface, **When** they ask a question related to that text, **Then** the chatbot returns an answer based only on the selected text without referencing other parts of the book.
2. **Given** a student has selected text that doesn't contain information needed to answer their question, **When** they ask the question, **Then** the chatbot informs them that the selected text doesn't contain the required information.

---

### User Story 3 - Evidence-based Responses (Priority: P3)

Student receives responses that include references to specific sections/chunks of the textbook that support the answer.

**Why this priority**: This enhances learning by allowing students to verify the source of information and explore related content.

**Independent Test**: Can be tested by asking questions and verifying that responses include specific references to textbook sections/chunks that support the answer.

**Acceptance Scenarios**:
1. **Given** a student asks a question, **When** the chatbot responds, **Then** the response includes specific references to textbook sections/chunks that were used to generate the answer.
2. **Given** a student wants to verify information from the chatbot response, **When** they access the provided references, **Then** they can see the original content that supports the answer.

---

## Edge Cases

- What happens when a question requires information from multiple unrelated parts of the book?
- How does the system handle ambiguous queries that could refer to different sections?
- What happens when the selected text is too small to provide meaningful context?
- How does the system respond when no relevant content is found in the textbook for a query?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST retrieve relevant textbook content from Qdrant based on user queries
- **FR-002**: System MUST differentiate between full-book queries and user-selected text queries
- **FR-003**: Users MUST be able to switch between full-book and selected-text query modes
- **FR-004**: System MUST provide evidence-based responses with references to specific textbook sections/chunks
- **FR-005**: System MUST integrate seamlessly with the frontend at hackathon-1-giaic.vercel.app
- **FR-006**: System MUST operate within free-tier service limitations including reasonable rate limiting to prevent exceeding quotas
- **FR-007**: System MUST NOT provide answers based on external knowledge beyond the textbook content

### Key Entities

- **Query**: A question or request for information from the textbook, with associated mode (full-book or selected-text)
- **Textbook Content**: Pre-indexed chunks of the textbook stored in Qdrant with metadata and references
- **Response**: Answer to the user's query with evidence references and source citations
- **User Selection**: Highlighted text in the textbook that constrains the scope of the query

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can get accurate answers to general textbook questions within 3 seconds of submitting their query
- **SC-002**: 95% of user-selected text queries return responses that are properly constrained to the selected content only
- **SC-003**: 90% of responses include specific references to textbook sections/chunks that support the answer
- **SC-004**: The chatbot successfully integrates with the frontend interface without performance degradation
- **SC-005**: The system operates within free-tier service limits throughout the hackathon period

## Clarifications

### Session 2025-12-16

- Q: The specification mentions "accurate answers" and "relevant" responses but lacks specific metrics. How should we define and measure accuracy and relevance for the RAG chatbot responses? → A: Accuracy = Responses must cite specific textbook sections that contain the answer; Relevance = All cited sections must be within 2 paragraphs of the actual answer
- Q: How should the system handle user sessions and message history? The constraint section mentions "no user authentication or long-term personalization" but doesn't specify short-term conversation context. → A: No message history - Each query is stateless and independent
- Q: For the RAG functionality, what should be the retrieval parameters for getting relevant chunks from Qdrant? Specifically, how many top-k results to retrieve and whether to implement reranking. → A: Top-k=5, with reranking - Retrieve 10, then rerank top 5 using cross-encoder for better relevance
- Q: How should the system handle errors and rate limiting, especially considering the free-tier service limitations? → A: Hybrid approach - Basic rate limiting on client, comprehensive error handling on server
- Q: What protocol should be used for communication between the frontend at hackathon-1-giaic.vercel.app and the backend API? → A: RESTful API with JSON - Standard HTTP requests with JSON payloads