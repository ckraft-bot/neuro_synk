import streamlit as st  
import streamlit.components.v1 as components

st.title("Interactive 3D Rubik's Cube")  
st.write("Solve or play with the Rubik’s Cube below!")  

# Embed an interactive Rubik's Cube from CodePen
components.iframe("https://codepen.io/oliverbenns/full/LYpQybz", height=600)
