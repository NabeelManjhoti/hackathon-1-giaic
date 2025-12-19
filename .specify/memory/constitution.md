<!-- SYNC IMPACT REPORT
Version change: N/A (initial version) → 1.0.0
Modified principles: N/A
Added sections: All principles (as initial constitution)
Removed sections: N/A
Templates requiring updates:
  - .specify/templates/plan-template.md (constitution check section) ⚠ pending - future implementations should validate against new principles
  - .specify/templates/spec-template.md (no changes needed) ✅ verified
  - .specify/templates/tasks-template.md (no changes needed) ✅ verified
Follow-up TODOs: None
-->

# Integrated RAG Chatbot for AI-native Textbook (Physical AI & Humanoid Robotics) Constitution

## Core Principles

### Grounded Accuracy
Responses only from retrieved textbook content or user-selected text; No external knowledge or hallucinations allowed

### Strict RAG Implementation
Dual-mode support: Full-book queries + user-selected text only; Reliable retrieval from Qdrant

### Reliable Retrieval
Fast, relevant chunks from Qdrant; Pre-indexed textbook embeddings

### Contextual Handling
Explicitly support user-highlighted text as isolated context

### Seamless Integration
Integrate with frontend at hackathon-1-giaic.vercel.app; Free-tier only services

### Low-latency Real-time Responses
Fast response times for real-time chatbot interactions; Performance optimization required

## Technology Stack Standards

Tech stack: OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres (metadata), Qdrant Cloud Free Tier (vectors)

## Development Workflow

End-to-end deployment; Functional embedded chatbot enhancing learning; Code quality, testing, performance, security, and architecture principles as per code standards

## Governance

All implementations must follow grounded accuracy principles; No hallucinations allowed; Strict adherence to RAG-only responses; Compliance with free-tier service limitations

**Version**: 1.0.0 | **Ratified**: 2025-12-16 | **Last Amended**: 2025-12-16