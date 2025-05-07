import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import importlib
 
# Set page configuration (MUSS die erste Streamlit-Funktion sein)
st.set_page_config(page_title="Chemie Dashboard", layout="wide")
 
# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_Daten")  # switch drive
 
# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page
 
# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df',
    file_name='data.csv',
    initial_value=pd.DataFrame(),
    parse_dates=['timestamp']
)
 
# --- Neues modernes Design mit Glassmorphism und Farbverläufen ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');
 
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        font-family: 'Inter', sans-serif;
        color: white;
    }
 
    .dashboard-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 20px;
    }
 
    .dashboard-card:hover {
        transform: scale(1.02);
        box-shadow: 0 16px 40px rgba(0, 255, 255, 0.3);
    }
 
    .center-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        color: #f1f2f6;
    }
 
    .dashboard-button {
        background: linear-gradient(90deg, #3498db, #8e44ad);
        color: white;
        padding: 12px 28px;
        border: none;
        border-radius: 12px;
        font-size: 16px;
        cursor: pointer;
        margin-top: 15px;
        transition: background 0.3s ease;
    }
 
    .dashboard-button:hover {
        background: linear-gradient(90deg, #8e44ad, #3498db);
    }
</style>
""", unsafe_allow_html=True)
 
st.markdown("<h1 class='center-title'>🔬 Chemie-Tool Dashboard</h1>", unsafe_allow_html=True)
 
# Seiten-Setup
seiten = {
    "🧪 Konzentrationen": "konzentrationen",
    "💧 Lösungen": "loesungen",
    "⚖️ Massenrechner": "massenrechner",
    "🔬 Periodensystem": "periodensystem",
    "🧫 pH-Rechner": "ph_rechner",
    "🧠 Quiz": "quiz",
    "📋 Säure-Base-Tabelle": "saeure_base_tabelle",
    "📓 Tagebuch": "tagebuch"
}
 
if "seite" not in st.session_state:
    st.session_state.seite = None
 
# Layout mit Karten
keys = list(seiten.keys())
cols = st.columns(2)
for i, key in enumerate(keys):
    with cols[i % 2]:
        st.markdown(f"<div class='dashboard-card'><h3>{key}</h3>", unsafe_allow_html=True)
        if st.button(f"🚀 {key} öffnen", key=key):
            st.session_state.seite = seiten[key]
 
# Ausgewählte Seite anzeigen
if st.session_state.seite:
    modulname = f"pages.{st.session_state.seite}"
    try:
        seite = importlib.import_module(modulname)
        if hasattr(seite, "app"):
            seite.app()
        else:
            st.warning(f"❌ Die Seite '{modulname}' hat keine Funktion namens app().")
    except Exception as e:
        st.error(f"💥 Fehler beim Laden von '{modulname}': {e}")