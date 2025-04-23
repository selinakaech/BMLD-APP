# ====== Start Login Block ======
from utils.login_manager import LoginManager
import streamlit as st

# Set page configuration (MUSS die erste Streamlit-Funktion sein)
st.set_page_config(page_title="LabMate", layout="centered")

# Login-Check
LoginManager().go_to_login('Start.py')
# ====== End Login Block ======

# Main title
st.markdown("<h1 style='text-align: center;'>Willkommen bei LabMate</h1>", unsafe_allow_html=True)

# Settings button (top-right)
st.markdown(
    """
    <style>
    .settings-button {
        position: absolute;
        top: 10px;
        right: 10px;
    }
    </style>
    <a href='/settings' target='_self' class='settings-button'>
        <button>⚙️ Einstellungen</button>
    </a>
    """,
    unsafe_allow_html=True,
)

# Buttons for page navigation
st.markdown("### Wählen Sie eine Seite:")
pages = {
    "Konzentrationen": "Konzentrationen.py",
    "Lösungen": "Lösungen.py",
    "Massenrechner": "Massenrechner.py",
    "Periodensystem": "Periodensystem.py",
    "pH-Rechner": "pH-Rechner.py",
    "Quiz": "Quiz.py",
    "Säure-Base-Tabellen": "Säure-Base-Tabelle.py",
    "Tagebuch": "Tagebuch.py",
}

for page_name, page_file in pages.items():
    if st.button(page_name):
        st.experimental_set_query_params(page=page_file)
        st.experimental_rerun()