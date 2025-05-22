import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import base64

# Funktion, um den Hintergrund per Bild-URL zu setzen
def set_background_from_url(image_url): 
    st.markdown(
        f"""
<style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.4)), 
                              url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: top; /* Verschiebt das Bild nach oben */
        }}
</style>
        """,
        unsafe_allow_html=True
    )

# Deine Bild-URL
image_url = "https://www.lebensmittelverband.de/fileadmin/_processed_/a/4/csm_AdobeStock_366724789_fotofabrika_2560x1340px_5055e2cdfc.jpg"

# Hintergrund setzen
set_background_from_url(image_url)


# --- Einführungstext ---
st.markdown("""
<div style='text-align: center; padding: 1rem 2rem; font-size: 1.1rem;'>
<h2>LabMate</h2>
<p>🔬 Willkommen in deiner persönlichen Chemie-Hilfe! 🧪<br>
Diese App ist dein vielseitiger Begleiter für chemische Aufgaben – egal ob in der Schule, im Studium oder beim Selbstlernen! 📚✨</p>
<p><strong>Hier findest du hilfreiche Tools wie:</strong></p>
<ul style="text-align: left; max-width: 600px; margin: 0 auto;">
  <li>Rechenhilfen (z. B. pH-Wert, Konzentrationen)</li>
  <li>Ein interaktives Periodensystem</li>
  <li>Unterstützung beim Umstellen von Formeln</li>
  <li>Und vieles mehr!</li>
</ul>
<p>📈 <strong>Behalte deinen Fortschritt im Blick!</strong><br>
Nutze die integrierte Lernkontrolle, um jederzeit zu sehen, wie weit du schon gekommen bist und woran du noch arbeiten möchtest.</p>
<p>📝 <strong>Lernaustausch inklusive!</strong><br>
Halte deine Gedanken, Erkenntnisse oder eigenen Erklärungen mit Datum fest – perfekt zum Nachschlagen oder als Austausch mit anderen Studierenden! 💡🗓️</p>
<p>Viel Spass beim Entdecken und Lernen! 🚀</p>
<p style="font-size: 0.9rem; color: gray;"><em>Diese App wurde von Soraya Gfrerer, Adriana Heeb und Selina Käch entwickelt.<br>
Kontakt: gfrersor@students.zhaw.ch, heebadr1@students.zhaw.ch, kaechsel@students.zhaw.ch</em></p>
</div>
""", unsafe_allow_html=True)

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_Daten")
login_manager = LoginManager(data_manager)
login_manager.login_register()

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )


# Einfügen des Logos in die Sidebar
# Funktion, um ein Bild in Base64 zu konvertieren
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Lokaler Pfad zum Bild
sidebar_logo_path = "docs/Images/Logo Labmate.png"  # Passe den Pfad an, falls nötig

# Lokaler Pfad zum Bild
sidebar_logo_path = "docs/Images/Logo Labmate.png"  # Passe den Pfad an, falls nötig

# Fehlerbehandlung für das Laden des Bildes
try:
    logo_base64 = get_base64_image(sidebar_logo_path)
    # Logo in der Sidebar einfügen
    st.sidebar.markdown(
        f"""
        <div style="text-align: center; padding: 10px 0;">
            <img src="data:image/png;base64,{logo_base64}" alt="Logo" style="width: 150px;">
        </div>
        """,
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.sidebar.error("Das Logo wurde nicht gefunden. Überprüfe den Pfad.")

