# filepath: c:\Users\soray\OneDrive - ZHAW\Studium Biomed. Labordiagnostik\MODULE\2. Semester\Informatik\BMLD_App_Chemie\BMLD-APP\pages\Konzentrationen.py

import streamlit as st

def app():
    st.title("Konzentrationen")
    st.write("Hier kannst du Konzentrationen berechnen.")
    n = st.number_input("Stoffmenge (mol)")
    V = st.number_input("Volumen (L)")
    if n > 0 and V > 0:
        c = n / V
        st.write(f"Konzentration: {c:.2f} mol/L")
    else:
        st.write("Bitte geben Sie gültige Werte für Stoffmenge und Volumen ein.")