import streamlit as st
import requests
import speech_recognition as sr
import time

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# Assistant Role Definition
SYSTEM_PROMPT = """
You are an empathetic and patient autism advocate. You are well-read in Cognitive, Clinical, and Personality Psychology and are skilled in understanding and supporting autistic individuals.
Be sure that you use "autistic" as a noun. For example, use "autistic individuals" or "autistics" instead of "individuals with autism" or "individuals on the autism spectrum".
If the user mentions suicidal ideation, do not engage or indulge just provide resources (e.g., hotlines) for mental health support.
You can:
- Help individuals regulate their emotions by providing coping strategies.
- Guide the individual through grounding techniques to reduce anxiety.
- Engage in friendly and supportive conversation.
"""

st.title("Neuro Synk Chat 💬")

with st.expander("ℹ️ Disclaimer"):
    st.caption(
        """
        I'm not a licensed therapist or medical professional. 
        If you're in an emergency, please call 911.
        Always talk to a qualified medical professional before making changes to your healthcare or lifestyle based on the information here.
        Don't ignore professional medical advice or delay seeking it because of something you read here.
        """
    )

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Speech-to-Text Function (Voice Input Only)
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... speak now!")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Speech recognition service is unavailable."
        except sr.WaitTimeoutError:
            return "No speech detected, please try again."

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User chooses input method
input_method = st.radio("Choose input method:", ["Type", "Speak"])

# Get user input
user_input = None
if input_method == "Type":
    user_input = st.chat_input("Ask me anything...")
elif input_method == "Speak":
    if st.button("🎤 Speak Now"):
        user_input = recognize_speech()
        if user_input:
            st.success(f"🎙️ You said: {user_input}")

# Process User Input
if user_input:
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
        full_prompt = f"{SYSTEM_PROMPT}\n\nConversation History:\n{conversation_history}\n\nUser: {user_input}\nAssistant:"

        # Send request to Ollama (Gemma 2B)
        response = requests.post(OLLAMA_URL, json={"model": "gemma:2b", "prompt": full_prompt, "stream": False})

        # Handle response
        if response.status_code == 200:
            bot_reply = response.json()["response"]
        else:
            bot_reply = "Error: Unable to generate response."

        # Dynamic loading animation with dots
        loading_text = st.empty()
        dots = [".", "..", "..."]  # Animated dots
        for i in range(15):  # Control how many times the animation should loop
            time.sleep(0.5)  # Adjust this value for animation speed
            loading_text.markdown(f"**Generating response{dots[i % len(dots)]}**")

        # Replace the animation with the final response
        loading_text.empty()
        typing_placeholder.markdown(bot_reply)

    # Add assistant response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
