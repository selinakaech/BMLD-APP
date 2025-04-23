from utils.login_manager import LoginManager
import streamlit as st

# Set page configuration (MUSS die erste Streamlit-Funktion sein)
st.set_page_config(page_title="LabMate", layout="centered")

# Login-Check
LoginManager().go_to_login('Start.py')

# Main title
st.markdown("<h1 style='text-align: center;'>Willkommen bei LabMate</h1>", unsafe_allow_html=True)

# Buttons for page navigation
st.markdown("### Wählen Sie eine Seite:")
pages = {
    "Konzentrationen": "Konzentrationen",
    "Lösungen": "Lösungen",
    "Massenrechner": "Massenrechner",
    "Periodensystem": "Periodensystem",
    "pH-Rechner": "pH-Rechner",
    "Quiz": "Quiz",
    "Säure-Base-Tabelle": "Säure-Base-Tabelle",
    "Tagebuch": "Tagebuch",
}

# Navigation zwischen den Seiten
for page_name, page_file in pages.items():
    if st.button(page_name):
        # Navigiere zur entsprechenden Seite
        st.experimental_set_query_params(page=page_file)
        st.experimental_rerun()