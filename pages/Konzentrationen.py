# ====== Start Login Block ======
from utils.login_manager import LoginManager
import streamlit as st

# Überprüfen, ob der Benutzer eingeloggt ist
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    LoginManager().go_to_login('Start.py')
    st.stop()  # Stoppt die Ausführung, bis der Benutzer eingeloggt ist
# ====== End Login Block ======

import streamlit as st

# Konzentration berechnen
st.title("Konzentration berechnen")
n = st.number_input("Stoffmenge (mol)")
V = st.number_input("Volumen (L)")
if n and V:
    c = n / V
    st.write(f"Konzentration: {c:.2f} mol/L")