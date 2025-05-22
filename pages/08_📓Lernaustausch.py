# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
from datetime import datetime
import base64

# Funktion, um den Hintergrund per Bild-URL zu setzen
def set_background_from_url(image_url): 
    st.markdown(
        f"""
<style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.4)), 
                              url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: top; /* Verschiebt das Bild nach oben */
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
        with open("lernaustausch.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""

# Funktion zum Speichern eines neuen Eintrags
def save_entry(entry):
    with open("lernaustausch.txt", "a", encoding="utf-8") as file:
        file.write(entry)

# --- UI-Logik ---
st.title("📓 Lernaustausch")
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
        username = st.session_state.get("username", "Unbekannt")
        entry = f"{timestamp} - {username}\n{new_entry.strip()}\n\n"
        save_entry(entry)
        st.success("Eintrag wurde gespeichert!")
        st.rerun()  # Seite neu laden nach dem Speichern
    else:
        st.warning("Der Eintrag darf nicht leer sein.")

# Einfügen des Logos in die Sidebar
# Funktion, um ein Bild in Base64 zu konvertieren
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Lokaler Pfad zum Bild
sidebar_logo_path = "docs/Images/Logo Labmate.png"  # Passe den Pfad an, falls nötig

# Lokaler Pfad zum Bild
sidebar_logo_path = "docs/Images/Logo Labmate.png"  # Passe den Pfad an, falls nötig

# Fehlerbehandlung für das Laden des Bildes
try:
    logo_base64 = get_base64_image(sidebar_logo_path)
    # Logo in der Sidebar einfügen
    st.sidebar.markdown(
        f"""
        <div style="text-align: center; padding: 10px 0;">
            <img src="data:image/png;base64,{logo_base64}" alt="Logo" style="width: 150px;">
        </div>
        """,
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.sidebar.error("Das Logo wurde nicht gefunden. Überprüfe den Pfad.")