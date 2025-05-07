import streamlit as st
import json
import os

@st.cache_data
def load_elements():
    # Dynamischer Pfad zur JSON-Datei im Ordner "script"
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Verzeichnis der aktuellen Datei
    script_dir = os.path.join(base_dir, "..", "script")  # Gehe in den Ordner "script"
    file_path = os.path.join(script_dir, "PeriodicTableJSON.json")
    
    # Datei öffnen und Daten laden
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return {el["symbol"]: el for el in data["elements"]}

def app():
    elements = load_elements()

    st.title("Periodensystem der Elemente")
    st.write("Geben Sie ein Elementsymbol ein (z. B. H, O, Fe):")
    symbol = st.text_input("Element").capitalize()

    if symbol in elements:
        el = elements[symbol]
        st.subheader(f"{el['name']} ({symbol})")
        st.write(f"**Ordnungszahl:** {el['number']}")
        st.write(f"**Molmasse:** {el['atomic_mass']} u")
        st.write(f"**Elektronegativität:** {el.get('electronegativity_pauling', 'nicht verfügbar')}")
        st.write(f"**Aggregatzustand:** {el.get('phase', 'unbekannt')}")
        st.write(f"**Dichte:** {el.get('density', 'unbekannt')} g/cm³")
        st.write(f"**Kategorie:** {el.get('category', 'nicht angegeben')}")
        st.write(f"**Aussehen:** {el.get('appearance', 'nicht angegeben')}")
        wiki_url = el.get("source", "")
        if wiki_url:
            st.markdown(f"[Weitere Informationen bei Wikipedia]({wiki_url})")
    elif symbol:
        st.error("Element nicht gefunden. Bitte überprüfen Sie das Symbol.")
    else:
        st.info("Bitte geben Sie ein Elementsymbol ein.")