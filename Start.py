import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import importlib
 
# Set page configuration
st.set_page_config(page_title="Chemie Dashboard", layout="wide")
 
# Initialize data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_Daten")
 
# Initialize login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()
 
# Load user data
data_manager.load_user_data(
    session_state_key='data_df',
    file_name='data.csv',
    initial_value=pd.DataFrame(),
    parse_dates=['timestamp']
)
 
# Custom CSS with Glassmorphism and Chemistry Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');
 
    .stApp {
        background: url('https://your-chemistry-themed-background-image.jpg') no-repeat center center fixed;
        background-size: cover;
        font-family: 'Inter', sans-serif;
    }
 
    .dashboard-card {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        transition: transform 0.3s ease;
    }
 
    .dashboard-card:hover {
        transform: scale(1.05);
    }
 
    h1, h2, h3, p {
        color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)
 
st.markdown("<h1 class='center-title'>🔬 Chemie-Tool Dashboard</h1>", unsafe_allow_html=True)
 
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
 
st.markdown("<hr>", unsafe_allow_html=True)
 
st.markdown("<p class='center-title'>Wähle ein Tool aus und leg los!</p>", unsafe_allow_html=True)

# Dashboard layout with cool chemical icons
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
cols = st.columns(3)
 
for i, name in enumerate(keys):
    with cols[i % 3]:
        with st.form(f"form_{i}"):
            st.markdown(f"<div class='dashboard-card'><h3>{name}</h3>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Öffnen")
            if submitted:
                st.session_state.seite = seiten[name]
 
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