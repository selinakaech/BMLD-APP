# ====== Start Login Block ======
from utils.login_manager import LoginManager
import streamlit as st

# Überprüfen, ob der Benutzer eingeloggt ist
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    LoginManager().go_to_login('Start.py')
    st.stop()  # Stoppt die Ausführung, bis der Benutzer eingeloggt ist
# ====== End Login Block ======

import streamlit as st
import math
import pandas as pd
import numpy as np

# Quiz-Seite
st.title("Quiz")
st.write("Fragen:")
st.text("1. ...")
st.text("2. ...")
st.text("3. ...")
if st.button("Antworten abschicken"):
    st.success("Antworten gespeichert (Demo)")