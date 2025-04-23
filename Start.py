# ====== Start Init Block ======
# This needs to copied on top of the entry point of the app (Start.py)
 
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
 
# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_Daten")  # switch drive
 
# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page
 
# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df',
    file_name='data.csv',
    initial_value = pd.DataFrame(),
    parse_dates = ['timestamp']
    )
# ====== End Init Block ======
 
 
import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
import importlib
 
st.set_page_config(page_title="Chemie Dashboard", layout="wide")
 
# --- Hintergrund mit modernem Glassmorphism ---
st.markdown("""
<style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');
 
        .stApp {
            background: linear-gradient(135deg, #e0f7fa, #f1f2f6);
            font-family: 'Inter', sans-serif;
        }
 
        .dashboard-card {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
            transition: all 0.3s ease-in-out;
            margin-bottom: 25px;
        }
 
        .dashboard-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0, 255, 255, 0.4);
            border: 1px solid rgba(0, 255, 255, 0.5);
        }
 
        .dashboard-button {
            background: linear-gradient(90deg, #2c3e50, #1abc9c);
            color: white;
            padding: 10px 25px;
            border: none;
            border-radius: 12px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 15px;
            transition: background 0.3s ease;
        }
 
        .dashboard-button:hover {
            background: linear-gradient(90deg, #1abc9c, #16a085);
        }
 
        .center-title {
            text-align: center;
            color: #2c3e50;
            font-weight: 700;
        }
 
        h3 {
            color: #2c3e50;
            margin-bottom: 10px;
        }
</style>
""", unsafe_allow_html=True)
 
st.markdown("<h1 class='center-title'>🔬 Chemie-Tool Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p class='center-title'>Wähle ein Tool aus und leg los!</p>", unsafe_allow_html=True)
 
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
<p>Viel Spaß beim Entdecken und Lernen! 🚀</p>
<p style="font-size: 0.9rem; color: gray;"><em>Diese App wurde von Soraya Gfrerer, Adriana Heeb und Selina Käch entwickelt.<br>
Kontakt: gfrersor@students.zhaw.ch, heebadr1@students.zhaw.ch, kaechsel@students.zhaw.ch</em></p>
</div>
""", unsafe_allow_html=True)
 
st.markdown("<hr>", unsafe_allow_html=True)
 
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
    try:
        seite = importlib.import_module(modulname)
        st.success(f"✅ Modul '{modulname}' wurde geladen.")
        st.write(f"🔎 Hat app(): {hasattr(seite, 'app')}")
 
        if hasattr(seite, "app"):
            seite.app()
        else:
            st.warning(f"❌ Die Seite '{modulname}' hat keine Funktion namens `app()`.")
    except Exception as e:
        st.error(f"💥 Fehler beim Laden von '{modulname}': {e}")