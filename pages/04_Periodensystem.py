# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import json
import os
 
@st.cache_data
def load_elements():
    # Dynamischer Pfad zur JSON-Datei
    file_path = os.path.join(os.path.dirname(__file__), "PeriodicTableJSON.json")
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return {el["symbol"]: el for el in data["elements"]}
 
def app():
    elements = load_elements()
    # Titel und Einführung mit Emojis
    st.title("🌍 Periodensystem der Elemente 🧪")
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