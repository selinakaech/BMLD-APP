# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
from datetime import datetime

# Funktion, um den Hintergrund per Bild-URL zu setzen
def set_background_from_url(image_url): 
    st.markdown(
        f"""
<style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
</style>
        """,
        unsafe_allow_html=True
    )

# Deine Bild-URL
image_url = "https://images.pexels.com/photos/4238510/pexels-photo-4238510.jpeg?auto=compress&cs=tinysrgb&w=1200&lazy=load"

# Hintergrund setzen
set_background_from_url(image_url)

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

# --- UI-Logik ---
st.title("📓 Tagebuch")
st.write("Hier kannst du deine Gedanken, Erkenntnisse oder Notizen festhalten.")

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
        st.experimental_rerun()  # Seite neu laden nach dem Speichern
    else:
        st.warning("Der Eintrag darf nicht leer sein.")