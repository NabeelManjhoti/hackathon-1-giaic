---
description: "Task list for Integrated RAG Chatbot implementation"
---

# Tasks: Integrated RAG Chatbot

**Input**: Design documents from `/specs/1-integrated-rag-chatbot/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in backend/
- [X] T002 [P] Initialize Python project with FastAPI, OpenAI, Qdrant, Pydantic dependencies in backend/requirements.txt
- [X] T003 [P] Configure linting and formatting tools (black, flake8, mypy) in backend/

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Set up Qdrant vector store connection in backend/src/core/vector_store.py
- [X] T005 [P] Implement embedding service using OpenAI text-embedding-3-small in backend/src/services/embedding_service.py
- [X] T006 [P] Setup API routing and middleware structure in backend/src/api/main.py
- [X] T007 Create base models/entities that all stories depend on in backend/src/models/
- [X] T008 Configure error handling and logging infrastructure in backend/src/core/
- [X] T009 Setup environment configuration management in backend/src/core/config.py
- [X] T010 [P] Implement rate limiting middleware for free-tier compliance in backend/src/middleware/

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Full-book RAG Query (Priority: P1) 🎯 MVP

**Goal**: Student asks general questions about the textbook content and receives accurate, context-aware responses based on the entire book

**Independent Test**: Can be fully tested by submitting questions to the chatbot and verifying that responses are accurate and sourced from the textbook content in Qdrant

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T011 [P] [US1] Contract test for full-book query endpoint in backend/tests/contract/test_full_book_query.py
- [ ] T012 [P] [US1] Integration test for full-book RAG flow in backend/tests/integration/test_full_book_rag.py

### Implementation for User Story 1

- [X] T013 [P] [US1] Create Query model in backend/src/models/query.py
- [X] T014 [P] [US1] Create Response model in backend/src/models/response.py
- [X] T015 [US1] Implement RAGService in backend/src/services/rag_service.py (depends on T005, T007)
- [X] T016 [US1] Implement full-book query endpoint in backend/src/api/rag_endpoints.py
- [X] T017 [US1] Add validation and error handling for full-book queries
- [X] T018 [US1] Add logging for user story 1 operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - User-selected Text Query (Priority: P2)

**Goal**: Student highlights specific text in the textbook and asks questions only about that selected text, receiving responses constrained to the selected content

**Independent Test**: Can be tested by selecting specific text portions and verifying that responses are restricted to information within the selected text only

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T019 [P] [US2] Contract test for selected-text query endpoint in backend/tests/contract/test_selected_text_query.py
- [ ] T020 [P] [US2] Integration test for selected-text RAG flow in backend/tests/integration/test_selected_text_rag.py

### Implementation for User Story 2

- [X] T021 [P] [US2] Create UserSelection model in backend/src/models/user_selection.py
- [X] T022 [US2] Implement selected-text query endpoint in backend/src/api/rag_endpoints.py
- [X] T023 [US2] Update RAGService to handle selected-text mode with direct injection approach (from research.md)
- [X] T024 [US2] Add validation and error handling for selected-text queries
- [X] T025 [US2] Integrate with User Story 1 components (if needed)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Evidence-based Responses (Priority: P3)

**Goal**: Student receives responses that include references to specific sections/chunks of the textbook that support the answer

**Independent Test**: Can be tested by asking questions and verifying that responses include specific references to textbook sections/chunks that support the answer

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T026 [P] [US3] Contract test for evidence-based response endpoint in backend/tests/contract/test_evidence_response.py
- [ ] T027 [P] [US3] Integration test for reference citation functionality in backend/tests/integration/test_references.py

### Implementation for User Story 3

- [X] T028 [P] [US3] Update Response model to include reference tracking in backend/src/models/response.py
- [X] T029 [US3] Implement reference extraction in backend/src/services/reference_service.py
- [X] T030 [US3] Update RAGService to include references in responses
- [X] T031 [US3] Update API endpoints to return responses with references
- [X] T032 [US3] Add confidence scoring to responses

**Checkpoint**: All user stories should now be independently functional

---
[Add more user story phases as needed, following the same pattern]

---
## Phase 6: Data Ingestion & Vector Indexing

**Goal**: Implement the data ingestion pipeline to index textbook content into Qdrant

- [X] T033 Create textbook ingestion service in backend/src/services/ingestion_service.py
- [X] T034 Implement chunking logic for textbook content in backend/src/core/chunking.py
- [X] T035 [P] Implement embedding and indexing pipeline in backend/src/services/indexing_service.py
- [X] T036 Create ingestion CLI command in backend/src/cli/ingest.py
- [X] T037 Add metadata extraction for textbook sections in backend/src/core/metadata_extraction.py

---
## Phase 7: ChatKit Integration

**Goal**: Integrate with OpenAI ChatKit SDKs for conversation handling

- [X] T038 [P] Set up ChatKit configuration in backend/src/core/chat_config.py
- [X] T039 Implement ChatKit wrapper service in backend/src/services/chat_service.py
- [X] T040 Integrate ChatKit with RAGService for enhanced responses
- [X] T041 Add streaming response support in backend/src/api/stream_endpoints.py

---
## Phase 8: Testing & Deployment

**Goal**: Comprehensive testing and deployment setup

- [ ] T042 Unit tests for retrieval relevance in backend/tests/unit/test_retrieval.py
- [ ] T043 Performance tests to ensure <200ms response time in backend/tests/performance/
- [ ] T044 [P] End-to-end tests for all user stories in backend/tests/e2e/
- [X] T045 Create Dockerfile for containerization in backend/Dockerfile
- [X] T046 Set up deployment configuration for Vercel in backend/vercel.json

---
## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T047 [P] Documentation updates in docs/
- [ ] T048 Code cleanup and refactoring
- [ ] T049 Performance optimization across all stories
- [ ] T050 [P] Additional unit tests (if requested) in backend/tests/unit/
- [ ] T051 Security hardening
- [ ] T052 Run quickstart.md validation

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Data Ingestion (Phase 6)**: Can run in parallel with user stories but required for full functionality
- **ChatKit Integration (Phase 7)**: Depends on User Story 1 completion
- **Testing & Deployment (Phase 8)**: Can run in parallel with other phases
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence