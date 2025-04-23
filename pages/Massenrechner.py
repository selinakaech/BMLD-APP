# ====== Start Login Block ======
from utils.login_manager import LoginManager
import streamlit as st

# Überprüfen, ob der Benutzer eingeloggt ist
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    LoginManager().go_to_login('Start.py')
    st.stop()  # Stoppt die Ausführung, bis der Benutzer eingeloggt ist
# ====== End Login Block ======

import streamlit as st

# Massenrechner
st.title("Massenrechner")
masse = st.number_input("Masse (g)")
molare_masse = st.number_input("Molmasse (g/mol)")
if masse and molare_masse:
    stoffmenge = masse / molare_masse
    st.write(f"Stoffmenge: {stoffmenge:.3f} mol")