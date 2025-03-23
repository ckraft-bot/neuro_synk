import streamlit as st  
import streamlit.components.v1 as components

st.title("Solve the cube")
st.write("Interactive 3D Rubik’s Cube")

# Embed an interactive Rubik's Cube from CodePen
components.iframe("https://codepen.io/oliverbenns/full/LYpQybz", height=600)
