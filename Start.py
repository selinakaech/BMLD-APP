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

    .dashboard-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 2rem;
    }

    .dashboard-card {
        font-size: 3.5rem;
        padding: 4rem;
        margin: 1rem 0;
        text-align: center;
        background-color: #ffffffdd;
        border-radius: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        transition: transform 0.2s ease-in-out;
        font-weight: bold;
        color: #000000;
        width: 100%;
        max-width: 1200px;
    }

    .dashboard-card:hover {
        transform: scale(1.05);
        background-color: #e0f7ff;
    }
</style>
""", unsafe_allow_html=True)

# --- Einführungstext ---
st.markdown("""
<div style='text-align: center; padding: 1rem 2rem; font-size: 1.1rem;'>
<h2>LabMate</h2>
<p>🔬 Willkommen in deiner persönlichen Chemie-Hilfe! 🧪<br>
Diese App ist dein vielseitiger Begleiter für chemische Aufgaben – egal ob in der Schule, im Studium oder beim Selbstlernen! 📚✨</p>
<p><strong>Hier findest du hilfreiche Tools wie:</strong></p>
<ul style="text-align: left; max-width: 600px; margin: 0 auto;">
<li>🔹 Rechenhilfen (z. B. pH-Wert, Konzentrationen)</li>
<li>🔹 Ein interaktives Periodensystem</li>
<li>🔹 Unterstützung beim Umstellen von Formeln</li>
<li>🔹 Und vieles mehr!</li>
</ul>
<p>📈 <strong>Behalte deinen Fortschritt im Blick!</strong><br>
Nutze die integrierte Lernkontrolle, um jederzeit zu sehen, wie weit du schon gekommen bist und woran du noch arbeiten möchtest.</p>
<p>📝 <strong>Lerntagebuch inklusive!</strong><br>
Halte deine Gedanken, Erkenntnisse oder eigenen Erklärungen mit Datum fest – perfekt zum Nachschlagen oder als persönliches Lernarchiv! 💡🗓️</p>
<p>Viel Spass beim Entdecken und Lernen! 🚀</p>
<p style="font-size: 0.9rem; color: gray;"><em>Diese App wurde von Soraya Gfrerer, Adriana Heeb und Selina Käch entwickelt.<br>
Kontakt: gfrersor@students.zhaw.ch, heebadr1@students.zhaw.ch, kaechsel@students.zhaw.ch</em></p>
</div>
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

st.markdown("<div class='dashboard-container'>", unsafe_allow_html=True)
for name, modul in module_dict.items():
    if st.button(name, key=modul):
        st.session_state.seite = modul
st.markdown("</div>", unsafe_allow_html=True)

# --- Modul laden ---
if st.session_state.seite:
    modulname = f"pages.{st.session_state.seite}"
    try:
        seite = importlib.import_module(modulname)
        if hasattr(seite, "app"):
            seite.app()
    except Exception as e:
        st.error(f"💥 Fehler beim Laden von '{modulname}': {e}")