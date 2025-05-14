# filepath: c:\Users\soray\OneDrive - ZHAW\Studium Biomed. Labordiagnostik\MODULE\2. Semester\Informatik\BMLD_App_Chemie\BMLD-APP\pages\Konzentrationen.py

import streamlit as st

# set_page_config muss als erste Streamlit-Anweisung stehen
st.set_page_config(page_title="Konzentrationsrechner", page_icon="⚗️", layout="centered")

st.markdown(
    """
<style>
    .main {background: linear-gradient(135deg, #4f8bff, #c0e8ff); color: #fff; font-family: Arial, sans-serif;}
    .stButton > button {background-color: #1f2937; color: #fff; font-size: 18px; padding: 10px 20px; border-radius: 10px;}
    input {font-size: 18px; padding: 10px; border-radius: 10px; border: 1px solid #ddd;}
    .result {font-size: 24px; margin-top: 20px; text-align: center;}
</style>
    """,
    unsafe_allow_html=True
)

st.title("⚗️ Konzentrationsrechner")
st.write("Hier kannst du Konzentrationen berechnen.")

n = st.number_input("Stoffmenge (mol)", min_value=0.0, format="%.4f")
V = st.number_input("Volumen (L)", min_value=0.0, format="%.4f")

if st.button("Berechnen"):
    if n > 0 and V > 0:
        c = n / V
        st.markdown(f'<div class="result">Konzentration: {c:.2f} mol/L</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result">Bitte geben Sie gültige Werte ein.</div>', unsafe_allow_html=True)