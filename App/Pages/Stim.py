import streamlit as st 
import streamlit.components.v1 as components
from streamlit_drawable_canvas import st_canvas
import numpy as np
import pandas as pd
import pydeck as pdk

st.title("Stim")

tool = st.sidebar.selectbox("Choose a fidget tool:", ["Light Switch", "Rubik's Cube", "Sand Drawing"])

# ------------------------------------------
# Light Switch (On/Off)
# ------------------------------------------
if tool == "Light Switch":
    st.subheader("Interactive Light Switch")

    # Toggle switch: Turns light on/off
    light_on = st.checkbox("Toggle the light switch on/off", value=False)

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
        # Play sound when light is turned on
        st.audio("\neuro_synk\Extras\switch-1.mp3") 

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
        # Play sound when light is turned off
        st.audio("\neuro_synk\Extras\switch-1.mp3") 

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