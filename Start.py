import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import importlib
 
# --- Page Configuration ---
st.set_page_config(page_title="Chemie Dashboard", layout="wide", initial_sidebar_state="collapsed")
 
# --- Funktion: Hintergrundbild setzen ---
def set_background_from_url(image_url):
    st.markdown(
        f"""
<style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
</style>
        """,
        unsafe_allow_html=True
    )
 
# --- Hintergrundbild-URL ---
image_url = "https://www.lebensmittelverband.de/fileadmin/_processed_/a/4/csm_AdobeStock_366724789_fotofabrika_2560x1340px_5055e2cdfc.jpg"
set_background_from_url(image_url)
 
# --- Benutzerdefiniertes CSS-Styling ---
st.markdown("""
<style>
    [data-testid="collapsedControl"] { display: none; }
    section[data-testid="stSidebar"] { display: none; }
 
    .dashboard-card {
        font-size: 3.5rem;
        padding: 4rem;
        margin-bottom: 1.5rem;
        text-align: center;
        background-color: #ffffffdd;
        border-radius: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        transition: transform 0.2s ease-in-out;
        font-weight: bold;
        color: #000000; /* Dunkelstes Schwarz */
        width: 95%; /* Fast Fensterbreit */
        max-width: 95%;
        margin-left: auto;
        margin-right: auto;
    }
 
    .dashboard-card:hover {
        transform: scale(1.05);
        background-color: #e0f7ff;
    }
</style>
""", unsafe_allow_html=True)
 
# --- Einführungstext ---
st.markdown("""
<h2>LabMate</h2>
<p>🔬 Willkommen in deiner persönlichen Chemie-Hilfe! 🧪</p>
<ul>
<li>🔹 Rechenhilfen (pH-Wert, Konzentrationen)</li>
<li>🔹 Interaktives Periodensystem</li>
<li>🔹 Unterstützung beim Umstellen von Formeln</li>
<li>🔹 Und vieles mehr!</li>
</ul>
<p>📈 Behalte deinen Fortschritt im Blick!</p>
""", unsafe_allow_html=True)
 
# --- Initialisierung ---
if "seite" not in st.session_state:
    st.session_state.seite = None
 
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_Daten")
login_manager = LoginManager(data_manager)
login_manager.login_register()
 
data_manager.load_user_data(
    session_state_key='data_df',
    file_name='data.csv',
    initial_value=pd.DataFrame(),
    parse_dates=['timestamp']
)
 
# --- Navigation ---
module_dict = {
    "⚙️ Einstellungen": "settings",
    "🧪 Konzentrationen": "konzentrationen",
    "⚖️ Massenrechner": "massenrechner",
    "🔬 Periodensystem": "periodensystem",
    "🧫 pH-Rechner": "ph_rechner",
    "📋 Säure-Base-Tabelle": "saeure_base_tabelle",
    "🧠 Quiz": "quiz",
    "📓 Tagebuch": "tagebuch"
}
 
for name, modul in module_dict.items():
    if st.button(name, key=modul):
        st.session_state.seite = modul
 
# --- Modul laden ---
if st.session_state.seite:
    modulname = f"pages.{st.session_state.seite}"
    try:
        seite = importlib.import_module(modulname)
        if hasattr(seite, "app"):
            seite.app()
    except Exception as e:
        st.error(f"💥 Fehler beim Laden von '{modulname}': {e}")