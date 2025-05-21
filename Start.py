import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

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
image_url = "https://www.lebensmittelverband.de/fileadmin/_processed_/a/4/csm_AdobeStock_366724789_fotofabrika_2560x1340px_5055e2cdfc.jpg"

# Hintergrund setzen
set_background_from_url(image_url)

with open("einleitung.md", "r", encoding="utf-8") as f:
    einleitung_text = f.read()

st.markdown(einleitung_text)

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