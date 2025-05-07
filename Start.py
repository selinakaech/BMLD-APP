# ====== Start Init Block ======
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
 
        .center-title {
            text-align: center;
            margin-top: 1rem;
        }
 
        h1.center-title {
            font-size: 3rem;
            margin-bottom: 0.5rem;
            color: #003366;
        }
 
        p.center-title {
            font-size: 1.2rem;
            color: #336699;
        }
 
        .dashboard-card {
            background-color: #ffffffdd;
            padding: 1.5rem;
            border-radius: 1rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.2s ease-in-out;
            text-align: center;
        }
 
        .dashboard-card:hover {
            transform: scale(1.02);
            background-color: #f1faff;
        }
 
        .dashboard-card h3 {
            margin-top: 0;
            font-size: 1.5rem;
            color: #003366;
        }
 
        ul li::before {
            content: "🧪 ";
            margin-right: 0.3em;
        }
</style>
""", unsafe_allow_html=True)
 
# Hintergrundmuster mit Chemie-Symbolen
st.markdown("""
<style>
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url("data:image/svg+xml;utf8,
<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200' viewBox='0 0 200 200'>
<text x='10' y='40' font-size='26' fill='rgba(0,0,0,0.04)' font-family='monospace'>:Cl:</text>
<text x='80' y='30' font-size='26' fill='rgba(0,0,0,0.04)' font-family='monospace'>H:</text>
<text x='140' y='50' font-size='26' fill='rgba(0,0,0,0.04)' font-family='monospace'>•</text>
<text x='60' y='120' font-size='30' fill='rgba(0,0,0,0.035)' font-family='monospace'>⚗️</text>
<text x='110' y='160' font-size='30' fill='rgba(0,0,0,0.035)' font-family='monospace'>🧪</text>
<text x='10' y='190' font-size='26' fill='rgba(0,0,0,0.04)' font-family='monospace'>/\\</text>
<text x='150' y='190' font-size='20' fill='rgba(0,0,0,0.04)' font-family='monospace'>e⁻</text>
</svg>");
            background-repeat: repeat;
            background-size: 200px;
            z-index: -1;
        }
</style>
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
# ====== End Init Block ======
 
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
 
# Navigation
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
 
# Modul laden
if st.session_state.seite:
    modulname = f"pages.{st.session_state.seite}"
    try:
        seite = importlib.import_module(modulname)
        st.success(f"✅ Modul '{modulname}' wurde geladen.")
        if hasattr(seite, "app"):
            seite.app()
        else:
            st.warning(f"❌ Die Seite '{modulname}' hat keine Funktion namens `app()`.")
    except Exception as e:
        st.error(f"💥 Fehler beim Laden von '{modulname}': {e}")