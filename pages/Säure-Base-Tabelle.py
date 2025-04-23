# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd
import numpy as np

# Definiere die app()-Funktion
def app():
    # Säure-Base-Tabelle
    st.title("Säure-Base-Tabelle")
    saure = st.text_input("Geben Sie eine Säure ein")
    base = st.text_input("Geben Sie eine Base ein")
    if saure or base:
        st.write(f"pKs-Wert (Demo): 4.75")