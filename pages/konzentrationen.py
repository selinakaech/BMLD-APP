import streamlit as st

# set_page_config muss als erste Streamlit-Anweisung stehen
st.set_page_config(page_title="Konzentrationsrechner", page_icon="⚗️", layout="centered")

# CSS für benutzerdefinierte Gestaltung
st.markdown(
    """
    <style>
        .main {background: linear-gradient(135deg, #4f8bff, #c0e8ff); color: #000; font-family: Arial, sans-serif;}
        .stButton > button {background-color: #1f2937; color: #fff; font-size: 18px; padding: 10px 20px; border-radius: 10px;}
        input {font-size: 18px; padding: 10px; border-radius: 10px; border: 1px solid #ddd;}
        .result {font-size: 24px; margin-top: 20px; text-align: center; color: #1f2937;}
        .title {text-align: center; font-size: 32px; color: #1f2937; margin-bottom: 20px;}
    </style>
    """,
    unsafe_allow_html=True
)

# Titel und Beschreibung
st.markdown('<div class="title">⚗️ Konzentrationsrechner</div>', unsafe_allow_html=True)
st.write("Hier kannst du Konzentrationen berechnen. Bitte gib die Werte für Stoffmenge und Volumen ein.")

# Eingabefelder
n = st.number_input("Stoffmenge (mol)", min_value=0.0, format="%.4f")
V = st.number_input("Volumen (L)", min_value=0.0, format="%.4f")

# Berechnung und Ausgabe
if st.button("Berechnen"):
    if n > 0 and V > 0:
        c = n / V
        st.markdown(f'<div class="result">Konzentration: {c:.2f} mol/L</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result">Bitte geben Sie gültige Werte ein.</div>', unsafe_allow_html=True)