# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd
import altair as alt
from functions.Molmassencalculator import create_result_dict
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
image_url = "https://images.pexels.com/photos/10187632/pexels-photo-10187632.jpeg?auto=compress&cs=tinysrgb&w=1200" 

# Hintergrund setzen
set_background_from_url(image_url)

# Titel und Einführung mit Emoji
st.title("⚖️ Molmassenrechner")
st.write(
    "Gib die chemische Formel (z.B. H₂O) und die gewünschte Menge ein - der Rechner berechnet die entsprechende Masse für dich. ⚗️"
)

with st.form(key='element_form'):
    compound = st.text_input('Geben Sie die chemische Verbindung ein (z.B. H2O):')
    multiplier = st.number_input('Geben Sie die entsprechende Menge der chemischen Verbindung ein:', min_value=1, value=1)
    submit_button = st.form_submit_button(label='Berechnen')
 
if submit_button:
    if compound:
        result = create_result_dict(compound, multiplier)
        if 'error' not in result:
            st.write(f'Die Molmasse der Verbindung {compound} multipliziert mit {multiplier} ist {result["molar_mass"]} g/mol.')

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