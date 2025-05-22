# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import json
import os
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
    
# KORREKTE Bild-URL (ohne Zeilenumbruch und Textreste)
image_url = "https://images.unsplash.com/photo-1628864005140-7770b9b8e7dd?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Hintergrund setzen
set_background_from_url(image_url)

@st.cache_data
def load_elements():
    # Dynamischer Pfad zur JSON-Datei
    file_path = os.path.join(os.path.dirname(__file__), "PeriodicTableJSON.json")
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return {el["symbol"]: el for el in data["elements"]}

elements = load_elements()

# Titel und Einführung mit Emojis
st.title("🌍 Periodensystem der Elemente")
st.write("Geben Sie das Elementsymbol ein (z. B. **H**, **O**, **Fe**), um mehr darüber zu erfahren:")

# Eingabefeld für das Elementsymbol
symbol = st.text_input("🔎 Element", "").capitalize()

if symbol in elements:
    el = elements[symbol]
    # Anzeige der Elementinformationen
    st.subheader(f"🧬 **{el['name']} ({symbol})**")
    st.write(f"**Ordnungszahl:** {el['number']} 🧮")
    st.write(f"**Molmasse:** {el['atomic_mass']} u ⚖️")
    st.write(f"**Elektronegativität:** {el.get('electronegativity_pauling', 'nicht verfügbar')} ⚡")
    st.write(f"**Aggregatzustand:** {el.get('phase', 'unbekannt')} 🌡️")
    st.write(f"**Dichte:** {el.get('density', 'unbekannt')} g/cm³ 💠")
    st.write(f"**Kategorie:** {el.get('category', 'nicht angegeben')} 🏷️")
    st.write(f"**Aussehen:** {el.get('appearance', 'nicht angegeben')} 🎨")
    # Wenn eine Wikipedia-Quelle vorhanden ist
    wiki_url = el.get("source", "")
    if wiki_url:
        st.markdown(f"📖 [Weitere Informationen bei Wikipedia]({wiki_url})")
elif symbol:
    st.error("❌ **Element nicht gefunden**. Bitte überprüfen Sie das Symbol.")
else:
    st.info("ℹ️ **Bitte geben Sie ein Elementsymbol ein**, um Details zu sehen.")


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