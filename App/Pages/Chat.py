import streamlit as st
import requests
import speech_recognition as sr
import time
from utility import *

# Assistant Role Definitions
ALLY_PROMPT = """
You are an empathetic and patient autism advocate. You are well-read in Cognitive, Clinical, and Personality Psychology and are skilled in understanding and supporting autistic individuals.
Be sure that you use "autistic" as a noun. For example, use "autistic individuals" or "autistics" instead of "individuals with autism" or "individuals on the autism spectrum".
If the user mentions suicidal ideation, do not engage or indulge just provide resources (e.g., hotlines) for mental health support.
You will not use autism speaks for any of your resources or citations.
You can:
- Help individuals regulate their emotions by providing coping strategies.
- Guide the individual through grounding techniques to reduce anxiety.
- Engage in friendly and supportive conversation.
"""

PROFESSOR_PROMPT = """
You are a knowledgeable professor with expertise in various fields, including science, history, and literature.
You have a patient and understanding approach when interacting with curious individuals, especially those with autism.
Your goal is to engage in conversations that provide deep insights and allow for infodumping. 
If the user expresses curiosity or provides an infodump, engage thoughtfully, offering a structured and informative response. 
You can:
- Break down complex topics into digestible, clear explanations.
- Respond with enthusiasm when the user shares their knowledge or curiosities.
- Encourage exploration and intellectual discussion.
- Use precise language and provide examples to ensure clarity in your responses.
"""

st.title("Neuro Synk Chat 💬")

donate()

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# User selects role
role = st.radio("Choose an option:", ["Emotional Regulation", "Info Dump"])

# Display disclaimer only if "Emotional Regulation" role is selected
if role == "Emotional Regulation":
    with st.expander("ℹ️ Disclaimer"):
        st.caption(
            """
            I'm not a licensed therapist or medical professional. 
            If you're in an emergency, please call 911.
            Always talk to a qualified medical professional before making changes to your healthcare or lifestyle based on the information here.
            Don't ignore professional medical advice or delay seeking it because of something you read here.
            """
        )

# User selects input method
input_method = st.radio("Choose input method:", ["Type", "Speak"])

# Get user input
user_input = None
if input_method == "Type":
    user_input = st.chat_input("Ask me anything...")
elif input_method == "Speak":
    if st.button("🎤 Speak Now"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("🎤 Listening... Speak now!")
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                user_input = text
                st.success(f"🎙️ You said: {user_input}")
            except sr.UnknownValueError:
                user_input = "Sorry, I couldn't understand that."
            except sr.RequestError:
                user_input = "Speech recognition service is unavailable."
            except sr.WaitTimeoutError:
                user_input = "No speech detected, please try again."

# Process User Input
if user_input:
    # Set the appropriate system prompt based on the selected role
    system_prompt = ALLY_PROMPT if role == "Emotional Regulation" else PROFESSOR_PROMPT

    # Add user input to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Display user's message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Create a placeholder for the assistant's "typing" animation
    with st.chat_message("assistant"):
        typing_placeholder = st.empty()

        # Build conversation history as part of the prompt
        conversation_history = "\n".join(
            [f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state["messages"]]
        )

        # Send conversation history + new question to Ollama
        full_prompt = f"{system_prompt}\n\nConversation History:\n{conversation_history}\n\nUser: {user_input}\nAssistant:"

        # Send request to Ollama (Gemma 2B)
        response = requests.post(OLLAMA_URL, json={"model": "gemma2:2b", "prompt": full_prompt, "stream": False})

        # Handle response
        if response.status_code == 200:
            bot_reply = response.json()["response"]
        else:
            bot_reply = "Error: Unable to generate response."

        # Handle response
        if response.status_code == 200:
            bot_reply = response.json()["response"]
        else:
            try:
                error_message = response.json()  # Try to parse JSON error details
            except ValueError:
                error_message = response.text  # If not JSON, return raw text

            bot_reply = f"Error {response.status_code}: {error_message}"


        # Typing animation effect
        displayed_text = ""
        for char in bot_reply:
            displayed_text += char
            typing_placeholder.markdown(displayed_text + "▌")  # Cursor effect
            time.sleep(0.02)  # Adjust typing speed

        # Replace the animation with the final text
        typing_placeholder.markdown(bot_reply)

    # Add assistant response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
