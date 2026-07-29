# SANDI

**Support and Navigation through Digital Intelligence**

> A human-centered AI-assisted communication system that improves access to community resources for people experiencing homelessness through a low-barrier SMS communication pipeline.

---

## Overview

SANDI is a research-driven project that investigates how Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), and human-centered design can improve access to community resources for underserved populations.

Unlike traditional mobile applications, SANDI is designed as a **communication system** where the primary interaction occurs through SMS. Community providers and administrators support the system by maintaining and verifying resource information through a dashboard, allowing the AI to provide grounded and up-to-date guidance.

The initial prototype focuses on **bureaucratic eligibility navigation**, helping users understand eligibility requirements for public assistance programs using trusted documentation.

---

## Research Goals

The long-term vision of SANDI is to develop a trustworthy AI communication infrastructure that supports:

* Homeless resource navigation
* Healthcare accessibility
* Bureaucratic service eligibility
* Community resource discovery
* Follow-up support
* Responsible and explainable AI

Current research focuses on:

* Retrieval-Augmented Generation (RAG)
* Human-Computer Interaction (HCI)
* Constitutional AI
* Community-centered technology
* AI-assisted communication systems

---

## Version 1 Scope

The current prototype focuses on one question:

> **Can AI explain bureaucratic service eligibility using trusted documentation while remaining transparent about uncertainty?**

Version 1 includes:

* Eligibility document ingestion
* Retrieval-Augmented Generation (RAG)
* Local embedding generation
* Plain-language response generation
* Mock SMS interaction
* Source-aware responses

Version 1 intentionally excludes:

* Real SMS integration
* Provider dashboard
* User registration
* Live resource availability
* Real-time shelter capacity
* Mobile application

---

## System Architecture

SANDI is organized into three interconnected components.

### Component 1 — The Conversation

The primary communication interface between users and the system.

Current:

* Mock SMS interface

Future:

* SMS hotline
* Web chat
* Voice interface

---

### Component 2 — The System

The AI backend responsible for:

* Document ingestion
* Semantic retrieval
* Response generation
* Trust and safety validation
* Follow-up support

---

### Component 3 — The Network

Community providers and verified administrators maintain resource information through a supporting dashboard.

Examples include:

* Shelters
* Clinics
* Food banks
* Outreach organizations
* University partners
* Community volunteers

---

## Technical Stack

### Language

* Python

### Backend

* FastAPI

### Embedding Model

* FlagEmbedding
* BAAI BGE-M3

### Language Model

* Qwen3 8B (Ollama)

### Vector Database

Current:

* Local vector storage

Future:

* PostgreSQL + pgvector

### Retrieval

* Retrieval-Augmented Generation (RAG)

---

## Current Development Roadmap

### Phase 1

Research and system planning

* Literature review
* Requirement Analysis Document (RAD)
* System architecture
* Technical design

### Phase 2

RAG implementation

* Document ingestion
* Text chunking
* Embedding generation
* Retrieval pipeline

### Phase 3

AI response generation

* Prompt engineering
* Grounded responses
* Eligibility explanation
* Source attribution

### Phase 4

Backend API

* FastAPI
* Conversation endpoints
* Knowledge endpoints

### Phase 5

Communication layer

* Mock SMS
* Future SMS provider integration

### Phase 6

Community network

* Provider dashboard
* Administrative tools
* Resource management

---

## Repository Structure

```text
sandi/
├── README.md
├── docs/
├── data/
├── app/
│   ├── api/
│   ├── models/
│   ├── rag/
│   ├── safety/
│   ├── messaging/
│   ├── prompts/
│   ├── config.py
│   └── main.py
├── scripts/
└── tests/
```

---

## Current Milestone

The current milestone is to build a complete Retrieval-Augmented Generation pipeline for bureaucratic eligibility guidance.

Pipeline:

```text
Eligibility Documents
        ↓
Document Ingestion
        ↓
Text Chunking
        ↓
BGE-M3 Embeddings
        ↓
Vector Storage
        ↓
Semantic Retrieval
        ↓
Qwen3 Response Generation
        ↓
Plain-Language Guidance
```

---

## Project Status

Current stage:

* System architecture complete
* Requirement analysis complete
* RAG implementation in progress

Next milestone:

* Working eligibility question-answering prototype using official CalFresh and related documentation

---

## Long-Term Vision

SANDI is intended to evolve from a research prototype into a scalable AI communication platform.

Potential future deployments include:

* Homeless resource navigation
* Community health communication
* Post-appointment healthcare support
* Disaster response
* Public service accessibility

---

## License

This repository is currently under active research and development.

License information will be added prior to public release.
