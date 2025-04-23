import streamlit as st
import importlib

# Initialisiere Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = None

# Login-Funktion
def check_login():
    if not st.session_state.logged_in:
        st.warning("Du musst dich einloggen, um fortzufahren.")
        username = st.text_input("Benutzername:")
        password = st.text_input("Passwort:", type="password")
        if st.button("Einloggen"):
            # Beispielhafte Login-Logik
            if username == "admin" and password == "passwort":  # Beispiel für einfachen Login
                st.session_state.logged_in = True
                st.success("Erfolgreich eingeloggt!")
            else:
                st.error("Ungültige Anmeldedaten.")
    else:
        st.success("Du bist bereits eingeloggt!")
        st.write("Wähle eine Seite aus:")
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
        for page_name, page_file in pages.items():
            if st.button(page_name):
                st.session_state["page"] = page_file

# Hauptlogik
check_login()

# Lade die ausgewählte Seite
if st.session_state.logged_in and st.session_state.page:
    modulname = f"pages.{st.session_state.page}"
    try:
        seite = importlib.import_module(modulname)
        seite.app()
    except Exception as e:
        st.error(f"Fehler beim Laden der Seite '{modulname}': {e}")