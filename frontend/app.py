import streamlit as st
import requests

st.title("🎥 Video Annotation Chatbot")

user_input = st.text_input("Ask a question about the videos:")

if st.button("Ask") and user_input:

    try:
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": user_input},
            timeout=120
        )

        if response.status_code == 200:
            st.write("### Answer:")
            st.write(response.json()["answer"])
        else:
            st.error("Backend returned an error.")

    except Exception as e:
        st.error(f"Cannot connect to backend: {e}")