# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st

# Definiere die app()-Funktion
def app():
    # Periodensystem
    st.title("Periodensystem")
    st.write("Geben Sie ein Element ein:")
    element = st.text_input("Element")
    if element:
        st.write(f"Informationen zu: {element}")
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large_de.png", use_column_width=True)