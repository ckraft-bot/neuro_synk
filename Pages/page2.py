import streamlit as st
import requests

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# Assistant Role Definition
SYSTEM_PROMPT = """
You are an empathetic and patient autism advocate. You have a psychology background and are skilled in understanding and supporting autistic individuals.
You can:
- Help individuals regulate their emotions by providing coping strategies.
- Explain concepts in a clear and structured way.
- Engage in friendly and supportive conversation.
"""

st.title("💬 Neuro Synk Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input field
if user_input := st.chat_input("Ask me anything..."):
    # Add user input to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Display user's message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Create prompt with assistant instructions
    prompt = f"{SYSTEM_PROMPT}\nUser: {user_input}\nAssistant:"

    # Send request to Ollama (Gemma 2B)
    response = requests.post(OLLAMA_URL, json={"model": "gemma:2b", "prompt": prompt, "stream": False})

    # Handle response
    if response.status_code == 200:
        bot_reply = response.json()["response"]
    else:
        bot_reply = "Error: Unable to generate response."

    # Add assistant response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

    # Display assistant's response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
