import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import importlib
 
st.set_page_config(page_title="Chemie Dashboard", layout="wide", initial_sidebar_state="collapsed")
 
# 🎨 Benutzerdefiniertes CSS-Styling
st.markdown("""
<style>
        [data-testid="collapsedControl"] {
            display: none;
        }
        section[data-testid="stSidebar"] {
            display: none;
        }
 
        .stApp {
            background: linear-gradient(to bottom right, #f0f4f8, #e0ecf7);
            font-family: 'Inter', sans-serif;
        }
 
        .dashboard-card {
            font-size: 1.3rem;
            padding: 2rem;
            margin-bottom: 1rem;
            text-align: center;
            background-color: #ffffffdd;
            border-radius: 1rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            transition: transform 0.2s ease-in-out;
        }
 
        .dashboard-card:hover {
            transform: scale(1.05);
            background-color: #e0f7ff;
        }
 
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            padding: 1rem 0;
        }
</style>
""", unsafe_allow_html=True)
 
# Einführungstext
st.markdown("""
<div style='text-align: center; padding: 1rem 2rem; font-size: 1.1rem;'>
<h2>LabMate</h2>
<p>🔬 Willkommen in deiner persönlichen Chemie-Hilfe! 🧪<br>
Diese App ist dein vielseitiger Begleiter für chemische Aufgaben – egal ob in der Schule, im Studium oder beim Selbstlernen! 📚✨</p>
<p><strong>Hier findest du hilfreiche Tools wie:</strong></p>
<ul>
<li>🔹 Rechenhilfen (z. B. pH-Wert, Konzentrationen)</li>
<li>🔹 Ein interaktives Periodensystem</li>
<li>🔹 Unterstützung beim Umstellen von Formeln</li>
<li>🔹 Und vieles mehr!</li>
</ul>
<p>Viel Spass beim Entdecken und Lernen! 🚀</p>
</div>
""", unsafe_allow_html=True)
 
# Initialisierung
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_Daten")
login_manager = LoginManager(data_manager)
login_manager.login_register()
 
data_manager.load_user_data(
    session_state_key='data_df',
    file_name='data.csv',
    initial_value=pd.DataFrame(),
    parse_dates=['timestamp']
)
 
# Navigation
seiten = {
    "🧪 Konzentrationen": "konzentrationen",
    "⚖️ Massenrechner": "massenrechner",
    "🔬 Periodensystem": "periodensystem",
    "🧫 pH-Rechner": "ph_rechner",
    "🧠 Quiz": "quiz",
    "📈 Lernfortschritt": "lernfortschritt",
    "📋 Säure-Base-Tabelle": "saeure_base_tabelle",
    "📓 Tagebuch": "tagebuch"
}
 
if "seite" not in st.session_state:
    st.session_state.seite = None
 
st.markdown("<div class='grid-container'>", unsafe_allow_html=True)
 
for name, modul in seiten.items():
    if st.button(name, key=modul, help="Klicke, um das Modul zu öffnen"):
        st.session_state.seite = modul
 
st.markdown("</div>", unsafe_allow_html=True)
 
# Modul laden
if st.session_state.seite:
    modulname = f"pages.{st.session_state.seite}"
    try:
        seite = importlib.import_module(modulname)
        st.success(f"✅ Modul '{modulname}' wurde geladen.")
        if hasattr(seite, "app"):
            seite.app()
    except Exception as e:
        st.error(f"💥 Fehler beim Laden von '{modulname}': {e}")