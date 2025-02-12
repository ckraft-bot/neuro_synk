import streamlit as st
import requests
import time
from utility import donate

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# Assistant Role Definition (same for all tasks)
SYSTEM_PROMPT = """ 
You are a professional linguist, skilled in analyzing tone and translating text; you are designed to help autistic individuals with written communication. 
In your response you will provide clear, concise, and structured responses that are easy to understand.
You can:
- judge the tone of a given text (e.g., professional, sarcastic, neutral, aggressive),
- transform text into different tones (e.g., more formal, more friendly, more concise),
- or create social stories to help individuals understand social situations to reduce anxiety.
"""

st.title("Neuro Synk Tool ⚙️")

donate()

# User selects a task
task = st.segmented_control("How can I help you?", ["Judge Tone", "Translate Text", "Create Social Story"])

# Text input
user_input = st.text_area("Enter text here:")
tone_option = None
if task == "Translate Text":
    tone_option = st.selectbox("Choose a tone:", ["Assertive", "Empathetic", "Formal", "Friendly", "Humorous", "Informal", "Neutral", "Sarcastic"])

# Default initialization of prompt
prompt = SYSTEM_PROMPT

if st.button("✨ Synk Up! ✨"):
    if user_input:
        # Modify prompt based on task
        if task == "Judge Tone":
            prompt = f"{SYSTEM_PROMPT}\nAnalyze the tone of this text:\n\n{user_input}\n\nAssistant:"
        elif task == "Translate Text" and tone_option:
            prompt = f"{SYSTEM_PROMPT}\nRewrite this text in a more {tone_option.lower()} tone:\n\n{user_input}\n\nAssistant:"
        elif task == "Create Social Story":
            prompt = f"{SYSTEM_PROMPT}\nCreate a social story based on this text:\n\n{user_input}\n\nAssistant:"

        # Create an animated loading indicator
        loading_text = st.empty()
        dots = ["", ".", "..", "..."]
        for i in range(15):  # Control how many times the animation should loop
            time.sleep(0.3)  # Adjust this value for animation speed
            loading_text.markdown(f"**Generating response{dots[i % len(dots)]}**")

        # Send request to Ollama
        response = requests.post(OLLAMA_URL, json={"model": "gemma2:2b", "prompt": prompt, "stream": False})

        # Clear loading indicator once response is ready
        loading_text.empty()

        # Display response
        if response.status_code == 200:
            bot_reply = response.json()["response"]
            st.markdown(f"**Neuro Synk's Response:**\n\n{bot_reply}")
        else:
            st.error("Error: Unable to generate response.")
