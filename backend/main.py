from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag_pipeline import get_rag_response

app = FastAPI()


# Request schema
class QueryRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(request: QueryRequest):
    answer = get_rag_response(request.question)
    return {"answer": answer}