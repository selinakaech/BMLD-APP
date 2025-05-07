import streamlit as st
from datetime import datetime

# Funktion zum Laden der Einträge
def load_entries():
    try:
        with open("tagebuch.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""

# Funktion zum Speichern eines neuen Eintrags
def save_entry(entry):
    with open("tagebuch.txt", "a", encoding="utf-8") as file:
        file.write(entry)

# Hauptfunktion der Seite
def app():
    st.title("Tagebuch")

    # Lade bestehende Einträge
    entries = load_entries()
    st.text_area("Einträge", entries, height=300, disabled=True)

    # Eingabefeld für neuen Eintrag
    new_entry = st.text_area("Neuer Eintrag", placeholder="Schreibe deinen Eintrag hier...")

    # Button zum Speichern des neuen Eintrags
    if st.button("Eintrag speichern"):
        if new_entry.strip():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"{timestamp}\n{new_entry.strip()}\n\n"
            save_entry(entry)
            st.success("Eintrag wurde gespeichert!")
            st.experimental_rerun()  # Seite neu laden, um die neuen Einträge anzuzeigen
        else:
            st.warning("Der Eintrag darf nicht leer sein.")