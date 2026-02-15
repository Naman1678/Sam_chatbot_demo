from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
import re

# Load everything once (better performance)
print("Loading embedding model...")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

print("Loading vector store...")
vector_store = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vector_store.as_retriever(search_kwargs={"k": 3})

print("Loading LLM...")
llm = OllamaLLM(model="phi3")


# Prompt template
prompt_template = """
You are a strict assistant that answers ONLY using the provided context.

IMPORTANT RULES:

- DO NOT use outside knowledge.
- DO NOT mention training data.
- DO NOT say you don't know unless context is empty.
- If the video exists in the context, answer using that description.

Context:
{context}

Question:
{question}

Answer based ONLY on the context above.
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)


def get_rag_response(question: str):

    match = re.search(r"(video\d+)", question.lower())

    if match:
        video_id = match.group(1)
        print(f"Detected explicit video ID: {video_id}")

        # Direct metadata search
        docs = vector_store.similarity_search(
            video_id,
            k=10
        )

        # Filter exact match
        docs = [
            d for d in docs
            if d.metadata.get("video_id", "").lower() == video_id
        ]

    else:
        # fallback semantic retrieval
        docs = retriever.invoke(question)

    # ---------- DEBUG ----------
    if not docs:
        print("NO DOCUMENTS FOUND")
    else:
        print("\nRetrieved docs:")
        for d in docs:
            print(d.page_content)

    # ---------- STEP 2: Build context ----------
    context = "\n".join([doc.page_content for doc in docs])

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    response = llm.invoke(final_prompt)

    return response


# Optional local testing
if __name__ == "__main__":
    while True:
        q = input("Ask: ")
        print(get_rag_response(q))