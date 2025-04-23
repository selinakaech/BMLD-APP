# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st

# Konzentration berechnen
st.title("Konzentration berechnen")
n = st.number_input("Stoffmenge (mol)")
V = st.number_input("Volumen (L)")
if n and V:
    c = n / V
    st.write(f"Konzentration: {c:.2f} mol/L")