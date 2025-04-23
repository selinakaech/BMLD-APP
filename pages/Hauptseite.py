from utils.login_manager import LoginManager
import streamlit as st

# Set page configuration (MUSS die erste Streamlit-Funktion sein)
st.set_page_config(page_title="LabMate", layout="centered")

# Login-Check
LoginManager().go_to_login('Start.py')

# Main title
st.markdown("<h1 style='text-align: center;'>Willkommen bei LabMate</h1>", unsafe_allow_html=True)

# Seitenüberschrift
st.markdown("### Wählen Sie eine Seite:")

# Seiten und ihre Namen
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

# Navigation zwischen den Seiten mit Markdown-Links
for page_name, page_file in pages.items():
    # Erstelle einen Markdown-Link für jede Seite
    st.markdown(f"- [Konzentrationen](/Konzentrationen)", unsafe_allow_html=True)
    st.markdown(f"- [Lösungen](/Lösungen)", unsafe_allow_html=True)
    st.markdown(f"- [Massenrechner](/Massenrechner)", unsafe_allow_html=True)
    st.markdown(f"- [Periodensystem](/Periodensystem)", unsafe_allow_html=True)
    st.markdown(f"- [pH-Rechner](/pH-Rechner)", unsafe_allow_html=True)
    st.markdown(f"- [Quiz](/Quiz)", unsafe_allow_html=True)
    st.markdown(f"- [Säure-Base-Tabelle](/Säure-Base-Tabelle)", unsafe_allow_html=True)
    st.markdown(f"- [Tagebuch](/Tagebuch)", unsafe_allow_html=True)