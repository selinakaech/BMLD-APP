# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')
# ====== End Login Block ======

import streamlit as st
import pandas as pd

# Vollständige Säure-Base-Tabelle
saeure_base_pks = pd.DataFrame([
    {"Säure": "HClO4 (Perchlorsäure)", "Base": "ClO4⁻ (Perchlorat)", "pKs": -9},
    {"Säure": "HCl (Chlorwasserstoff)", "Base": "Cl⁻ (Chlorid)", "pKs": -6},
    {"Säure": "H2SO4 (Schwefelsäure)", "Base": "HSO4⁻ (Hydrogensulfat)", "pKs": -3},
    {"Säure": "H3O⁺ (Hydronium)", "Base": "H2O (Wasser)", "pKs": -1.74},
    {"Säure": "HNO3 (Salpetersäure)", "Base": "NO3⁻ (Nitrat)", "pKs": -1.32},
    {"Säure": "HClO3 (Chlorsäure)", "Base": "ClO3⁻ (Chlorat)", "pKs": 0},
    {"Säure": "HOOCCOOH (Oxalsäure)", "Base": "HOOCCOO⁻ (Hydrogenoxalat)", "pKs": 1.46},
    {"Säure": "HSO4⁻ (Hydrogensulfat)", "Base": "SO4²⁻ (Sulfat)", "pKs": 1.92},
    {"Säure": "H2SO3 (Schweflige Säure)", "Base": "HSO3⁻ (Hydrogensulfit)", "pKs": 1.96},
    {"Säure": "H3PO4 (Phosphorsäure)", "Base": "H2PO4⁻ (Dihydrogenphosphat)", "pKs": 1.96},
    {"Säure": "Weinsäure", "Base": "Hydrogentartrat", "pKs": 3.00},
    {"Säure": "Zitronensäure", "Base": "Dihydrogencitrat", "pKs": 3.10},
    {"Säure": "HF (Fluorwasserstoff)", "Base": "F⁻ (Fluorid)", "pKs": 3.14},
    {"Säure": "HNO2 (Salpetrige Säure)", "Base": "NO2⁻ (Nitrit)", "pKs": 3.35},
    {"Säure": "HCOOH (Ameisensäure)", "Base": "HCOO⁻ (Formiat)", "pKs": 3.70},
    {"Säure": "CH3CHOHCOOH (Milchsäure)", "Base": "CH3CHOHCOO⁻ (Lactat)", "pKs": 3.87},
    {"Säure": "C6H5COOH (Benzoesäure)", "Base": "C6H5COO⁻ (Benzoat)", "pKs": 4.22},
    {"Säure": "Hydrogentartrat", "Base": "Tartrat", "pKs": 4.30},
    {"Säure": "HOOCCOO⁻ (Hydrogenoxalat)", "Base": "⁻OOCCOO⁻ (Oxalat)", "pKs": 4.40},
    {"Säure": "Dihydrogencitrat", "Base": "Hydrogencitrat", "pKs": 4.70},
    {"Säure": "CH3COOH (Essigsäure)", "Base": "CH3COO⁻ (Acetat)", "pKs": 4.72},
    {"Säure": "C3H7COOH (Buttersäure)", "Base": "C3H7COO⁻ (Butyrat)", "pKs": 4.82},
    {"Säure": "C2H5COOH (Propionsäure)", "Base": "C2H5COO⁻ (Propionat)", "pKs": 4.88},
    {"Säure": "Hydrogencitrat", "Base": "Citrat", "pKs": 5.40},
    {"Säure": "H2CO3 (Kohlensäure)", "Base": "HCO3⁻ (Hydrogencarbonat)", "pKs": 6.46},
    {"Säure": "H2S (Schwefelwasserstoff)", "Base": "HS⁻ (Hydrogensulfid)", "pKs": 7.06},
    {"Säure": "HSO3⁻ (Hydrogensulfit)", "Base": "SO3²⁻ (Sulfit)", "pKs": 7.20},
    {"Säure": "H2PO4⁻ (Dihydrogenphosphat)", "Base": "HPO4²⁻ (Hydrogenphosphat)", "pKs": 7.21},
    {"Säure": "HClO (Hypochlorsäure)", "Base": "ClO⁻ (Hypochlorit)", "pKs": 7.25},
    {"Säure": "NH4⁺ (Ammonium)", "Base": "NH3 (Ammoniak)", "pKs": 9.21},
    {"Säure": "HCN (Blausäure)", "Base": "CN⁻ (Cyanid)", "pKs": 9.40},
    {"Säure": "C6H5OH (Phenol)", "Base": "C6H5O⁻ (Phenolat)", "pKs": 9.89},
    {"Säure": "HCO3⁻ (Hydrogencarbonat)", "Base": "CO3²⁻ (Carbonat)", "pKs": 10.40},
    {"Säure": "HPO4²⁻ (Hydrogenphosphat)", "Base": "PO4³⁻ (Phosphat)", "pKs": 12.32},
    {"Säure": "HS⁻ (Hydrogensulfid)", "Base": "S²⁻ (Sulfid)", "pKs": 12.90},
    {"Säure": "H2O (Wasser)", "Base": "OH⁻ (Hydroxid)", "pKs": 15.74},
    {"Säure": "C2H5OH (Ethanol)", "Base": "C2H5O⁻ (Ethanolat)", "pKs": 16.00},
    {"Säure": "CH3COCH3 (Aceton)", "Base": "CH3COCH2⁻ (Acetonat)", "pKs": 19.00},
    {"Säure": "NH3 (Ammoniak)", "Base": "NH2⁻ (Dihydrogennitrid)", "pKs": 23.00}
])
 

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
image_url = "https://www.shutterstock.com/image-photo/buffer-solution-glass-chemical-laboratory-600nw-2215810923.jpg"
 
# Hintergrund setzen
set_background_from_url(image_url)

st.title("⚗️ Säure-Base-Tabelle")
 
st.write(
    "Gib den Namen einer **Säure** oder **Base** ein, um den zugehörigen **pKs-Wert** zu erhalten. "
    "Die Tabelle unten hilft dir bei der Auswahl. 🔍"
)
 
# Auswahl oder Eingabe einer Substanz
suchoptionen = pd.concat([saeure_base_pks["Säure"], saeure_base_pks["Base"]]).unique()
auswahl = st.selectbox("🔎 Substanz auswählen oder eintippen:", sorted(suchoptionen))
 
# Suche nach Substanz
zeile = saeure_base_pks[(saeure_base_pks["Säure"] == auswahl) | (saeure_base_pks["Base"] == auswahl)]
 
if not zeile.empty:
    st.success(
        f"✅ **Gefunden:**\n\n"
        f"- **Säure:** {zeile.iloc[0]['Säure']}\n"
        f"- **Base:** {zeile.iloc[0]['Base']}\n"
        f"- **pKs-Wert:** {zeile.iloc[0]['pKs']}"
    )
else:
    st.warning("⚠️ Keine passende Substanz gefunden.")
 
# Anzeige der gesamten Tabelle
st.subheader("📊 Vollständige Säure-Base-Tabelle")
st.dataframe(saeure_base_pks)