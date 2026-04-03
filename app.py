import streamlit as st
from rag_system.ingestion import sliding_window
from rag_system.pyramid import build_pyramid
from rag_system.retrieval import retrieve

st.set_page_config(page_title="RAG Demo", layout="wide")

st.title("🧠 RAG System with Knowledge Pyramid")

# Input text
text = st.text_area("📄 Enter your document:", height=200)

if text and len(text.strip()) > 20:
    chunks = sliding_window(text)

    if not chunks:
        st.error("⚠️ No valid content to process.")
        st.stop()

    kb, vectorizer = build_pyramid(chunks)

    query = st.text_input("🔍 Ask a question:")

    if query:
        result, score = retrieve(query, kb, vectorizer)

        if result:
            st.success(f"Confidence Score: {round(score * 100, 1)}%")

            st.subheader("📄 Summary")
            st.write(result["summary"])

            st.subheader("🏷️ Category")
            st.write(result["label"])

            st.subheader("🔑 Keywords")
            st.write(", ".join(result["keywords"]))

            st.subheader("📚 Raw Text")
            st.write(result["raw_text"])
        else:
            st.error("No result found")

else:
    st.info("👉 Please enter a meaningful document (at least 20+ characters).")