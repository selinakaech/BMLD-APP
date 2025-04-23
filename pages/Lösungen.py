# ====== Start Login Block ======
from utils.login_manager import LoginManager
import streamlit as st

# Überprüfen, ob der Benutzer eingeloggt ist
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    LoginManager().go_to_login('Start.py')
    st.stop()  # Stoppt die Ausführung, bis der Benutzer eingeloggt ist
# ====== End Login Block ======


import streamlit as st

# Lösungen
st.title("Lösungen")
st.line_chart([1, 3, 2, 4, 7, 5])  # Beispielhafte Fortschrittsgrafik