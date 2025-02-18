import streamlit as st
OLLAMA_URL = "http://157.230.187.207:11434" #"http://localhost:11434/api/generate" <-- local

def donate():
    """Streamlit donation options."""
    st.sidebar.markdown(
            '<a href="https://ko-fi.com/clairekraft" target="_blank">'
            '<img src="https://miro.medium.com/v2/resize:fit:1200/1*HdRAxEVwO_27UL1e6QhUeA.png" width="100" alt="Buy Me a Coffee">'
            '</a>',
            unsafe_allow_html=True
    )