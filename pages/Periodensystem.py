# ====== Start Login Block ======
from utils.login_manager import LoginManager
import streamlit as st

# Überprüfen, ob der Benutzer eingeloggt ist
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    LoginManager().go_to_login('Start.py')
    st.stop()  # Stoppt die Ausführung, bis der Benutzer eingeloggt ist
# ====== End Login Block ======

import streamlit as st

# Periodensystem
st.title("Periodensystem")
st.write("Geben Sie ein Element ein:")
element = st.text_input("Element")
if element:
    st.write(f"Informationen zu: {element}")
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large_de.png", use_column_width=True)