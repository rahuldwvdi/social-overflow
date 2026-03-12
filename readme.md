# Social Overflow

Social Overflow is a multi-agent AI debate platform.

Instead of a single AI answer, multiple AI agents propose arguments, critique each other, and a critic agent evaluates the best reasoning.

## Features

- Multi-agent reasoning
- AI debate engine
- Adversarial critique system
- Critic evaluation
- SQLite debate memory
- Context retrieval
- Local LLM runtime using Ollama
- FastAPI backend
- Simple web dashboard

## Tech Stack

Python  
FastAPI  
SQLite  
HTML/CSS/JS  
Ollama (TinyLlama)

## Example Flow

User Question → AI Agents Debate → Critiques → Critic Evaluation → Stored Debate

## Running Locally

Install dependencies:

pip install fastapi uvicorn requests

Run server:

uvicorn main:app --reload

Open:

http://localhost:8000/app