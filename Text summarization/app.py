import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("Text Summarizer using Langchain and Groq")
st.markdown("Paste your content and get a concise summary")

text_input = st.text_area("Enter the text to summarize", height=300)

if st.button("Summarize"):
    if text_input.strip():
        with st.spinner("Summarizing your content..."):
            summary = summarize_text(text_input)
            st.subheader("Summary")
            st.write(summary)
    else:
        st.warning("Please enter some text...")
