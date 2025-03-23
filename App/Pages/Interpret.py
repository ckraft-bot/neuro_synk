import streamlit as st
import requests
import time
from utility import *

# Assistant Role Definition (same for judge and translate tasks)
TOOL_PROMPT = """ 
You are a professional linguist, skilled in analyzing tone and translating text; you are designed to help autistic individuals with written communication. 
In your response you will provide clear, concise, and structured responses that are easy to understand.
You can:
- judge the tone of a given text (e.g., professional, sarcastic, neutral, aggressive),
- transform text into different tones (e.g., more formal, more friendly, more concise),
"""

STORY_PROMPT = """ 
You are a story teller who creates social stories to help individuals understand social situations to reduce anxiety. 
Social stories were created by Carol Gray in 1991. They are short descriptions of a particular situation, event or activity, which include specific information about what to expect in that situation and why. 

A social story needs to have a title, introduction, body and conclusion.
- It should be in paragraph form and the whole story in 3 paragraphs or less.
- It should be written in the first person, from the perspective of the autistic person.
- It should use gentle and supportive language. 
- It should answer six questions: where, when, who, what, how and why? 
- It should be made up of descriptive sentences, and may also have coaching sentences. A descriptive sentence accurately describes the context, such as where the situation occurs, who is there, what happens and why, for example: 

Social stories can be used to: 
- develop self-care skills (for example, how to clean teeth, wash hands or get dressed), social skills (for example, sharing, asking for help, saying thank you, interrupting) and academic abilities
- help someone to understand how others might behave or respond in a particular situation
- help others understand the perspective of an autistic person and why they may respond or behave in a particular way
- help a person to cope with changes to routine and unexpected or distressing events (for example, absence of teacher, moving house, thunderstorms)
- provide positive feedback to a person about an area of strength or achievement in order to develop self-esteem
- as a behavioural strategy (for example, what to do when angry, how to cope with obsessions). 


Here's an exmaple of a social story for Christmas:
Christmas Day is 25 December. 

Sometimes I get sick. 

My body needs food several times per day; just like a steam train needs coal to stay running. 

A coaching sentence gently guides behaviour, for example: 

I will try to hold an adult's hand when crossing the road. 

It's ok to ask an adult for help with nightmares. 

When I am angry, I can take three deep breaths, go for a walk or jump on the trampoline.
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
# prompt = SYSTEM_PROMPT

if st.button("✨ Synk Up! ✨"):
    if user_input:
        # Modify prompt based on task
        if task == "Judge Tone":
            prompt = f"{TOOL_PROMPT}\nAnalyze the tone of this text:\n\n{user_input}\n\nAssistant:"
        elif task == "Translate Text" and tone_option:
            prompt = f"{TOOL_PROMPT}\nRewrite this text in a more {tone_option.lower()} tone:\n\n{user_input}\n\nAssistant:"
        elif task == "Create Social Story":
            prompt = f"{STORY_PROMPT}\nCreate a social story based on this text:\n\n{user_input}\n\nAssistant:"

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
