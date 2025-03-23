import streamlit as st 
import streamlit.components.v1 as components
from streamlit_drawable_canvas import st_canvas
import numpy as np
import os
import pandas as pd
import pydeck as pdk

st.title("Stim")

tool = st.sidebar.selectbox("Choose a fidget tool:", ["Light Switch", "Rubik's Cube", "Sand Drawing"])

if tool == "Light Switch":
    st.subheader("Interactive Light Switch")

    # Toggle switch: Turns light on/off
    light_on = st.checkbox("Toggle the light switch on/off", value=False)

    # Absolute path to the audio file in the Extras folder
    audio_file = "C:\\Users\\Clair\\Documents\\GitHub\\neuro_synk\\Extras\\switch-1.mp3" 

    # Relative path to the audio file in the Extras folder
    # audio_file = os.path.join("Extras", "switch-1.mp3")
    
    if light_on:
        st.write("The light is ON")
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #FCF14E; /* Light yellow background */
            }
            </style>
            """, unsafe_allow_html=True
        )

    else:
        st.write("The light is OFF")
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #626164; /* Dark background */
            }
            </style>
            """, unsafe_allow_html=True
        )

# ------------------------------------------
# Rubik's Cube (Interactive)
# ------------------------------------------
elif tool == "Rubik's Cube":
    st.header("Interactive Rubik's Cube")
    components.iframe("https://codepen.io/bsehovac/full/EMyWVv", height=600)

# ------------------------------------------
# Sand Drawing (Interactive)
# ------------------------------------------
elif tool == "Sand Drawing":
    st.subheader("Sand Drawing")
    
    # Draw color and stroke size
    stroke_width = st.slider("Stroke Width", 1, 50, 3)
    stroke_color = st.color_picker("Stroke Color", "#654321")  # Sand-like color
    
    canvas_result = st_canvas(
        fill_color="#FFD700",  # Sand-like color
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color="#FFF8DC",  # Light sand color
        height=400,
        width=600,
        drawing_mode="freedraw",
        key="sand_canvas"
    )
    
    st.write("Use your mouse or touch input to draw in the sand!")