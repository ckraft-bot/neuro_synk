import streamlit as st
import requests
import time 

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# Assistant Role Definition
SYSTEM_PROMPT = """
You are an empathetic and patient autism advocate. You are well read in Cognitive, Clinical, and Personality Psychology and are skilled in understanding and supporting autistic individuals.
You can:
- Help individuals regulate their emotions by providing coping strategies.
- Engage in friendly and supportive conversation.
- Discourage suicidal ideation and provide resources for mental health support.
"""

st.title("Neuro Synk Chat:left_speech_bubble:")

with st.expander("ℹ️ Disclaimer"):
    st.caption(
        """
        I'm not a licensed therapist or medical professional. 
        If you're in an emergency, please call 911.
        Always talk to a qualified medical professional before making changes to your healthcare or lifestyle based on the information here.
        Don't ignore professional medical advice or delay seeking it because of something you read here.
        """
    )

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

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

    # Create a placeholder for the assistant's "typing" animation
    with st.chat_message("assistant"):
        typing_placeholder = st.empty()  # Placeholder for animation

        # Create prompt with assistant instructions
        prompt = f"{SYSTEM_PROMPT}\nUser: {user_input}\nAssistant:"

        # Send request to Ollama (Gemma 2B)
        response = requests.post(OLLAMA_URL, json={"model": "gemma:2b", "prompt": prompt, "stream": False})

        # Handle response
        if response.status_code == 200:
            bot_reply = response.json()["response"]
        else:
            bot_reply = "Error: Unable to generate response."

        # Typing animation effect
        displayed_text = ""
        for char in bot_reply:
            displayed_text += char
            typing_placeholder.markdown(displayed_text + "▌")  # Cursor effect
            time.sleep(0.02)  # Adjust speed here

        # Replace the animation with the final text
        typing_placeholder.markdown(bot_reply)

    # Add assistant response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
