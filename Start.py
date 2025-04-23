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

# Set page configuration
st.set_page_config(page_title="LabMate", layout="centered")

# Main title
st.title('LabMate')

# Willkommenstext
st.write("🔬 Willkommen in deiner persönlichen Chemie-Hilfe! 🧪")
st.write("""
Diese App ist dein vielseitiger Begleiter für chemische Aufgaben – egal ob in der Schule, im Studium oder beim Selbstlernen! 📚✨
Hier findest du hilfreiche Tools wie:

🔹 Rechenhilfen (z. B. pH-Wert, Konzentrationen)  
🔹 Ein interaktives Periodensystem  
🔹 Unterstützung beim Umstellen von Formeln  
🔹 Und vieles mehr!

📈 Behalte deinen Fortschritt im Blick! ✅  
Nutze die integrierte Lernkontrolle, um jederzeit zu sehen, wie weit du schon gekommen bist und woran du noch arbeiten möchtest.

📝 Lerntagebuch inklusive!  
Halte deine Gedanken, Erkenntnisse oder eigenen Erklärungen mit Datum fest – perfekt zum Nachschlagen oder als persönliches Lernarchiv! 💡🗓️

Viel Spaß beim Entdecken und Lernen! 🚀
""")

# Entwicklerinformationen
st.write("Diese App wurde von Soraya Gfrerer, Adriana Heeb und Selina Käch entwickelt.")
st.write("E-Mail Adressen: gfrersor@students.zhaw.ch, heebadr1@students.zhaw.ch, kaechsel@students.zhaw.ch")

# Seiten und ihre Namen
pages = {
    "Konzentrationen": "Konzentrationen",
    "Lösungen": "Lösungen",
    "Massenrechner": "Massenrechner",
    "Periodensystem": "Periodensystem",
    "pH-Rechner": "pH-Rechner",
    "Quiz": "Quiz",
    "Säure-Base-Tabelle": "Säure-Base-Tabelle",
    "Tagebuch": "Tagebuch",
}

# Buttons für die Navigation
st.markdown("### Wähle eine Seite aus:")
for page_name, page_file in pages.items():
    if st.button(page_name):
        # Setze die Query-Parameter für die Navigation
        st.experimental_set_query_params(page=page_file)
        st.experimental_rerun()