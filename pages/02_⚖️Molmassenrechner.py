# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd
import altair as alt
from functions.Molmassencalculator import create_result_dict

# Funktion, um den Hintergrund per Bild-URL zu setzen
def set_background_from_url(image_url): 
    st.markdown(
        f"""
<style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
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
    "Berechne die **Stoffmenge** aus der **Masse** und der **Molmasse**. "
    "Gib die Masse der Substanz und ihre Molmasse ein, um die Stoffmenge in Mol zu berechnen. 🔬"
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