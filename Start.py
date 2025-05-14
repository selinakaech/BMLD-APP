import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import importlib
 
st.set_page_config(page_title="Chemie Dashboard", layout="wide", initial_sidebar_state="collapsed")
 
# 🎨 Benutzerdefiniertes CSS-Styling
if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#f0f4f8"
 
if "symbol_pattern" not in st.session_state:
    st.session_state.symbol_pattern = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200' viewBox='0 0 200 200'><text x='10' y='40' font-size='26' fill='rgba(0,0,0,0.04)' font-family='monospace'>:Cl:</text></svg>"
 
# Settings
with st.sidebar:
    st.header("⚙️ Einstellungen")
    st.session_state.bg_color = st.color_picker("Hintergrundfarbe auswählen", value=st.session_state.bg_color)
    st.session_state.symbol_pattern = st.text_area("Symbol-Muster (SVG)", value=st.session_state.symbol_pattern)
 
st.markdown(f"""
<style>
        .stApp {{
            background: {st.session_state.bg_color};
            font-family: 'Inter', sans-serif;
            background-image: url('{st.session_state.symbol_pattern}');
            background-repeat: repeat;
            background-size: 200px;
        }}
 
        .grid-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            padding: 2rem 0;
        }}
 
        .dashboard-card {{
            font-size: 1.3rem;
            padding: 1.5rem;
            text-align: center;
            background-color: #ffffffdd;
            border-radius: 1rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            transition: transform 0.2s ease-in-out;
        }}
 
        .dashboard-card:hover {{
            transform: scale(1.05);
            background-color: #e0f7ff;
        }}
</style>
""", unsafe_allow_html=True)
 
# Einführungstext
st.markdown("""
<div style='text-align: center; padding: 1rem 2rem; font-size: 1.1rem;'>
<h2>LabMate</h2>
<p>🔬 Willkommen in deiner persönlichen Chemie-Hilfe! 🧪<br>
Diese App ist dein vielseitiger Begleiter für chemische Aufgaben – egal ob in der Schule, im Studium oder beim Selbstlernen! 📚✨</p>
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
 
st.markdown("<div class='grid-container'>", unsafe_allow_html=True)
 
for name, modul in seiten.items():
    if st.button(name, key=modul, help="Klicke, um das Modul zu öffnen", use_container_width=True):
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