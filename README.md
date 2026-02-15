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
```

2. Create Virtual Environment
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
Mac/Linux:
```bash
python -m venv venv
source venv/bin/activate
```
3. Install Requirements
```bash
pip install -r requirements.txt
```
4. Install Ollama
Download:
https://ollama.com

Check:
```bash
ollama --version
```

5. Pull Required Models
Open a NEW terminal:
```bash
ollama pull phi3
ollama pull nomic-embed-text
```

6. Generate Dataset File
```bash
python backend/data_loader.py
```

7. Build Vector Store
(Delete vector_store/ first if exists)
```bash
python backend/vector_store.py
```

8. Start Backend
```bash
uvicorn backend.main:app --reload
```

Backend runs at: http://127.0.0.1:8000

9. Start Frontend
New terminal:
```bash
streamlit run app.py
```
Open: http://localhost:8501
Example: what happens in video7135?