import streamlit as st
OLLAMA_URL = "http://157.230.187.207:11434" #"http://localhost:11434/api/generate" <-- local

def donate():
    """Streamlit donation options."""
    st.sidebar.markdown(
        '<a href="https://ko-fi.com/clairekraft" target="_blank">'
        '<img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" width="200" alt="Buy Me a Coffee">'
        '</a>',
        unsafe_allow_html=True
    )