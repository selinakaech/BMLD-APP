# ====== Start Login Block ======
from utils.login_manager import LoginManager
import streamlit as st

# Überprüfen, ob der Benutzer eingeloggt ist
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    LoginManager().go_to_login('Start.py')
    st.stop()  # Stoppt die Ausführung, bis der Benutzer eingeloggt ist
# ====== End Login Block ======

import streamlit as st
import pandas as pd
import numpy as np

# Säure-Base-Tabelle
st.title("Säure-Base-Tabelle")
saure = st.text_input("Geben Sie eine Säure ein")
base = st.text_input("Geben Sie eine Base ein")
if saure or base:
    st.write(f"pKs-Wert (Demo): 4.75")