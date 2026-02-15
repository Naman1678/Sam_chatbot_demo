import json
import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document


def create_vector_store():

    print("Creating vector store...")

    # Load annotation file
    with open("data/msrvtt_annotations.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []

    for item in data:

        # IMPORTANT: include video_id inside searchable text
        text_content = f"""
Video ID: {item['video_id']}
Description: {item['caption']}
"""

        documents.append(
            Document(
                page_content=text_content,
                metadata={
                    "video_id": item["video_id"]
                }
            )
        )

    print(f"Total documents prepared: {len(documents)}")

    # Use correct embedding model
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    print("Generating embeddings (this may take time)...")

    vector_store = FAISS.from_documents(documents, embeddings)

    # Save vector store
    os.makedirs("vector_store", exist_ok=True)
    vector_store.save_local("vector_store")

    print("✅ Vector store created and saved successfully.")


if __name__ == "__main__":
    create_vector_store()