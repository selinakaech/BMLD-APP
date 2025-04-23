# ====== Start Login Block ======
from utils.login_manager import LoginManager
import streamlit as st
import math  # Import für mathematische Funktionen

# Überprüfen, ob der Benutzer eingeloggt ist
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    LoginManager().go_to_login('Start.py')
    st.stop()  # Stoppt die Ausführung, bis der Benutzer eingeloggt ist
# ====== End Login Block ======

# pH-Rechner
st.title("pH-Rechner")
c_h3o = st.number_input("Konzentration [H₃O⁺] in mol/L")
if c_h3o > 0:
    ph = -math.log10(c_h3o)
    st.write(f"pH-Wert: {ph:.2f}")
else:
    st.write("Bitte geben Sie eine gültige Konzentration > 0 ein.")