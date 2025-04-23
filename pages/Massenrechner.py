# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st

# Massenrechner
st.title("Massenrechner")
masse = st.number_input("Masse (g)")
molare_masse = st.number_input("Molmasse (g/mol)")
if masse and molare_masse:
    stoffmenge = masse / molare_masse
    st.write(f"Stoffmenge: {stoffmenge:.3f} mol")