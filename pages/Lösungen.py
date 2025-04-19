# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st

# Lösungen
elif page == "Lösungen":
    st.title("Lösungen")
    st.line_chart([1, 3, 2, 4, 7, 5])  # Beispielhafte Fortschrittsgrafik