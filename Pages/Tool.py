import streamlit as st
import requests

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# Assistant Role Definition
SYSTEM_PROMPT = """ 
You are a professional linguist, skilled in analyzing tone and translating text; you are deigned to help autistic individuals with written communication. 
You can:
- Judge the tone of a given text (e.g., professional, sarcastic, neutral, aggressive).
- Transform text into different tones (e.g., more formal, more friendly, more concise).
- Create social stories to help individuals understand social situations to reduce anxiety.
- Provide clear, concise, and structured responses that are easy to understand.
"""

st.title("Neuro Synk Tool:gear:")

# User selects a task
task = st.segmented_control("How can I help you?", ["Judge Tone", "Translate Text", "Create Social Story"])

# Text input
user_input = st.text_area("Enter text here:")
tone_option = None
if task == "Translate Text":
    tone_option = st.selectbox("Choose a tone:", ["Assertive", "Empathetic", "Formal", "Friendly", "Humorous", "Informal", "Neutral", "Sarcastic"])

if st.button(":sparkles: Synk Up! :sparkles:"):
    if user_input:
        # Modify prompt based on task
        if task == "Judge Tone":
            prompt = f"{SYSTEM_PROMPT}\nAnalyze the tone of this text:\n\n{user_input}\n\nAssistant:"
        elif task == "Translate Text" and tone_option:
            prompt = f"{SYSTEM_PROMPT}\nRewrite this text in a more {tone_option.lower()} tone:\n\n{user_input}\n\nAssistant:"
        elif task == "Create Social Story":
            prompt = f"{SYSTEM_PROMPT}\nCreate a social story based on this text:\n\n{user_input}\n\nAssistant:"

        # Send request to Ollama
        response = requests.post(OLLAMA_URL, json={"model": "gemma:2b", "prompt": prompt, "stream": False})

        # Display response
        if response.status_code == 200:
            bot_reply = response.json()["response"]
            st.markdown(f"**Neuro Synk's Response:**\n\n{bot_reply}")
        else:
            st.error("Error: Unable to generate response.")
