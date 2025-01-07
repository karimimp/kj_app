import streamlit as st
from ruminants_calculation import *

st.header(f"Ruminants 🐃")

model_choice = st.sidebar.selectbox("Model: ", ( "antibiotics", 'reproduction'))
st.divider()
if model_choice == "antibiotics":
    antibiotics()
if model_choice == "reproduction":
    repro()

st.divider()