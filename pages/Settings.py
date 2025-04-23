# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st

# Settings
st.title("Einstellungen")
st.write("Hintergrundfarbe, Sprache, etc.")
st.write("Hier können Sie Ihre Einstellungen anpassen.")
st.write("Aktuelle Einstellungen:")      