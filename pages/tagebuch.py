import streamlit as st
from datetime import datetime

# Funktion zum Initialisieren des Tagebuchs im Session State
def initialize_tagebuch():
    if "tagebuch" not in st.session_state:
        st.session_state.tagebuch = []  # Liste für die Notizen

# Funktion zum Hinzufügen eines neuen Eintrags
def add_entry(entry_text):
    if entry_text.strip():  # Nur speichern, wenn der Text nicht leer ist
        st.session_state.tagebuch.append({
            "datum": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "text": entry_text.strip()
        })

# Funktion zum Rendern der Tagebuch-Seite
def app():
    st.title("📓 Tagebuch")
    st.write("Hier kannst du deine Gedanken, Erkenntnisse oder Notizen festhalten.")

    # Initialisiere das Tagebuch
    initialize_tagebuch()

    # Zeige bestehende Einträge
    st.subheader("Bisherige Einträge")
    if st.session_state.tagebuch:
        for entry in reversed(st.session_state.tagebuch):  # Neueste Einträge zuerst
            st.markdown(f"""
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 10px; margin-bottom: 10px; background-color: #f9f9f9;">
                <strong>{entry['datum']}</strong>
                <p>{entry['text']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Noch keine Einträge vorhanden. Schreibe unten einen neuen Eintrag, um zu beginnen.")

    # Bereich zum Hinzufügen eines neuen Eintrags
    st.subheader("➕ Neuer Eintrag")
    new_entry = st.text_area("Schreibe hier deinen neuen Eintrag:")
    if st.button("Speichern"):
        add_entry(new_entry)
        st.success("Eintrag gespeichert!")
        st.experimental_rerun()  # Seite neu laden, um den neuen Eintrag anzuzeigen