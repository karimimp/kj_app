import streamlit as st
from smallies_calculation import *

st.header(f"Smallies 🐕‍🦺")


model_choice = st.sidebar.selectbox("Model: ", ("💧 fluid", "💊 drug dosage", "🩸 blood transfusion", "💉 hypokalaemia","🍼 nutrition"))
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
st.divider()