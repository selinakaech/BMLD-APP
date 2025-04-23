# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.radio("Gehe zu", [
    "Startseite", 
    "Hauptseite", 
    "Periodensystem", 
    "Massenrechner", 
    "pH-Rechner", 
    "Säure-Base-Tabelle", 
    "Konzentration berechnen", 
    "Quiz", 
    "Lösungen", 
    "Settings"
])