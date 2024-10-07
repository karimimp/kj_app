import streamlit as st
from smallies_calculation import *

st.header(f"Smallies 🐕")


model_choice = st.sidebar.selectbox("Model: ", ("💧 fluid", "💊 drug dosage", "🩸 blood transfusion", "💉 hypokalaemia","🍼 nutrition", "parvo", 'shock','antidotes'))
st.divider()
if model_choice == "💧 fluid":
    fluid_calc()

elif model_choice == "💊 drug dosage":
    drug()

elif model_choice == "🩸 blood transfusion":
    blood()

elif model_choice == "💉 hypokalaemia":
    hypokalaemia()

elif model_choice == "🍼 nutrition":
    nutrition()

elif model_choice == "parvo":
    parvo()

elif model_choice == "shock":
    shock()
elif model_choice == "antidotes":
    antidotes()
st.divider()