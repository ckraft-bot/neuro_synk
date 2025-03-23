import streamlit as st 
import streamlit.components.v1 as components
from streamlit_drawable_canvas import st_canvas
import numpy as np
import pandas as pd
import pydeck as pdk

st.title("Stim")

tool = st.sidebar.selectbox("Choose a fidget tool:", ["Particle Effect", "Rubik's Cube", "Sand Drawing", ])

if tool == "Particle Effect":
    st.subheader("Interactive Particle Effect")

    num_particles = 500
    data = np.random.rand(num_particles, 2) * [360, 180]  # Lat/Lon scaling
    
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=pd.DataFrame(data, columns=["lon", "lat"]),
        get_position="[lon, lat]",
        get_radius=1000,
        get_fill_color="[200, 30, 0, 160]",
        pickable=True,
    )
    
    view_state = pdk.ViewState(latitude=0, longitude=0, zoom=1)
    
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

elif tool == "Rubik's Cube":
    st.header("Interactive Rubiks Cube")

    components.iframe("https://codepen.io/bsehovac/full/EMyWVv", height=600)

elif tool == "Sand Drawing":
    st.subheader("Sand Drawing")
    
    canvas_result = st_canvas(
        fill_color="#FFD700",  # Sand-like color
        stroke_width=3,
        stroke_color="#654321",  # Darker sand color
        background_color="#FFF8DC",  # Light sand color
        height=400,
        width=600,
        drawing_mode="freedraw",
        key="sand_canvas"
    )
    
    st.write("Use your mouse or touch input to draw in the sand!")


