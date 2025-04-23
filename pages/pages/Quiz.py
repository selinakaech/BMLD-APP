# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd
import numpy as np

# Definiere die app()-Funktion
def app():
    # Quiz-Seite
    st.title("Quiz")
    st.write("Fragen:")
    st.text("1. ...")
    st.text("2. ...")
    st.text("3. ...")
    if st.button("Antworten abschicken"):
        st.success("Antworten gespeichert (Demo)")