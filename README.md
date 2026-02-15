# Video Annotation RAG Chatbot (Ollama-Based)

## Overview

This project builds a Retrieval-Augmented Generation (RAG) chatbot that answers user questions based on video annotation files from the MSR-VTT dataset.

The system:
- Extracts video annotations
- Converts them into embeddings
- Stores them in a FAISS vector database
- Uses a local LLM (Ollama - Mistral) to generate grounded answers

---

## Tech Stack

- Python
- FastAPI
- LangChain
- FAISS
- Ollama (local LLM)
- MSR-VTT Dataset

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your_repo_url>
cd Sam_chatbot
