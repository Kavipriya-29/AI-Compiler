# AI Compiler for Software Generation

# Overview

AI Compiler is a multi-stage software generation system that converts natural language requirements into structured, validated, and executable application configurations.

The system behaves like a compiler:

Natural Language → Intent Extraction → System Design → Schema Generation → Validation → Repair → Runtime Execution

---

# Features

* Intent Extraction
* System Design Layer
* UI Schema Generation
* API Schema Generation
* Database Schema Generation
* Authentication Rules
* Validation Engine
* Repair Engine
* Runtime Execution Simulation
* Evaluation Metrics
* React Frontend Interface

---

# Architecture

User Prompt
↓
Intent Extraction
↓
System Design
↓
Schema Generation
↓
Validation Engine
↓
Repair Engine
↓
Runtime Execution
↓
Executable Application Configuration

---

# Backend

* FastAPI
* Gemini API
* Python

# Run Backend

```bash
cd backend
uvicorn main:app --reload
```

---

# Frontend

* React
* Vite

# Run Frontend

```bash
cd frontend
npm install
npm run dev
```

---

# Example Prompt

Build a CRM with login, contacts, dashboard, role-based access and payments.

---

# Evaluation

Dataset:
The project includes:

- 10 Real Product Prompts
- 10 Edge Case Prompts

Edge cases include:
- Vague requirements
- Missing specifications
- Contradictory requirements
- Incomplete requests

Metrics:

* Success Rate
* Failure Count
* Request Count
* Runtime Validation Score

---

# Future Improvements

* Full Runtime Code Generation
* Multi-Agent Architecture
* Dynamic Database Modeling
* Production Deployment Support

---

# Author

Kavipriya T

Artificial Intelligence and Data Science

SNS College of Engineering
