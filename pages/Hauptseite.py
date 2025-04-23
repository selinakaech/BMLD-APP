import streamlit as st
import importlib
 
st.set_page_config(page_title="Chemie Dashboard", layout="wide")
 
# --- Style für die Karten ---
st.markdown("""
<style>
        .dashboard-card {
            background: linear-gradient(135deg, #74ebd5 0%, #9face6 100%);
            padding: 25px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 4px 4px 20px rgba(0,0,0,0.1);
            margin-bottom: 25px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .dashboard-card:hover {
            transform: scale(1.03);
            box-shadow: 6px 6px 25px rgba(0,0,0,0.2);
        }
        .dashboard-button {
            background-color: #2c3e50;
            color: white;
            padding: 10px 25px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 15px;
        }
        .dashboard-button:hover {
            background-color: #1abc9c;
        }
        .center-title {
            text-align: center;
            color: #2c3e50;
        }
</style>
""", unsafe_allow_html=True)
 
st.markdown("<h1 class='center-title'>🔬 Chemie-Tool Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p class='center-title'>Wähle ein Tool aus und leg los!</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
 
# Seiten-Setup
seiten = {
    "🧪 Konzentrationen": "Konzentrationen",
    "💧 Lösungen": "Lösungen",
    "⚖️ Massenrechner": "Massenrechner",
    "🔬 Periodensystem": "Periodensystem",
    "🧫 pH-Rechner": "pH-Rechner",
    "🧠 Quiz": "Quiz",
    "📋 Säure-Base-Tabelle": "Säure-Base-Tabelle",
    "📓 Tagebuch": "Tagebuch"
}
 
if "seite" not in st.session_state:
    st.session_state.seite = None
 
# Layout mit Karten
keys = list(seiten.keys())
for i in range(0, len(keys), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(keys):
            name = keys[i + j]
            modul = seiten[name]
            with cols[j]:
                with st.form(f"form_{i+j}"):
                    st.markdown(f"<div class='dashboard-card'><h3>{name}</h3>", unsafe_allow_html=True)
                    submitted = st.form_submit_button("Öffnen", use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                    if submitted:
                        st.session_state.seite = modul
 
# Ausgewählte Seite anzeigen
if st.session_state.seite:
    modulname = f"pages.{st.session_state.seite}"
    seite = importlib.import_module(modulname)
    seite.app()