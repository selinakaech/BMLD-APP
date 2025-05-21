# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd

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
image_url = "https://www.shutterstock.com/image-photo/buffer-solution-glass-chemical-laboratory-600nw-2215810923.jpg"
 
# Hintergrund setzen
set_background_from_url(image_url)

# Titel und Einführung mit Emoji
st.title("⚗️ Säure-Base-Tabelle")
st.write(
    "Berechne und betrachte die **pKs-Werte** von Säuren und Basen. "
    "Geben Sie einfach den Namen einer Säure oder Base ein und erfahren Sie den zugehörigen pKs-Wert. 🔬"
)

# Eingabefelder für Säure und Base
saure = st.text_input("🔴 Geben Sie eine Säure ein (z.B. HCl)")
base = st.text_input("🔵 Geben Sie eine Base ein (z.B. NH3)")

# Tabelle mit pKs-Werten für gängige Säuren und Basen
pKs_wert = {
    "HClO4": -9, "HCl": -6, "H2SO4": -3, "H3O+": -1.74, "HNO3": -1.32,
    "HClO3": 0, "HOOCCOOH": 1.46, "HSO4-": 1.92, "H2SO3": 1.96, "H3PO4": 1.96,
    "Weinsäure": 3, "Zitronensäure": 3.1, "HF": 3.14, "HNO2": 3.35, "HCOOH": 3.7,
    "CH3CHOHCOOH": 3.87, "C6H5COOH": 4.22, "Hydrogentartrat": 4.3, "HOOCCOO-": 4.4,
    "Dihydrogencitrat": 4.7, "CH3COOH": 4.72, "C3H7COOH": 4.82, "C2H5COOH": 4.88,
    "Hydrogencitrat": 5.4, "H2CO3": 6.46, "H2S": 7.06, "HSO3-": 7.2, "H2PO4-": 7.21,
    "HClO": 7.25, "NH4+": 9.21, "HCN": 9.4, "C6H5OH": 9.89, "HCO3-": 10.4,
    "HPO4-": 12.32, "HS-": 12.9, "H2O": 15.74, "C2H5OH": 16, "CH3COCH3": 19,
    "NH3": 23
}

# Anzeige der Tabelle mit Beispielen
st.subheader("📊 Beispiel pKs-Werte")
pKs_df = pd.DataFrame(list(pKs_wert.items()), columns=["Substanz", "pKs-Wert"])
st.dataframe(pKs_df)

# Überprüfen, ob die eingegebene Säure oder Base einen pKs-Wert hat
if saure:
    saure = saure.strip()
    if saure in pKs_wert:
        st.success(f"Der pKs-Wert von **{saure}** ist: **{pKs_wert[saure]:.2f}**")
    else:
        st.warning(f"Für die Säure **{saure}** sind keine pKs-Werte verfügbar. Versuchen Sie es mit einer anderen Säure.")

if base:
    base = base.strip()
    if base in pKs_wert:
        st.success(f"Der pKs-Wert der Base **{base}** ist: **{pKs_wert[base]:.2f}**")
    else:
        st.warning(f"Für die Base **{base}** sind keine pKs-Werte verfügbar. Versuchen Sie es mit einer anderen Base.")

# Zusätzliche Tipps in einem Info-Fenster
st.info(
    "ℹ️ Tipp: Wenn Sie den pKs-Wert einer anderen Substanz suchen, versuchen Sie es mit einem der Beispiele aus der Tabelle oder geben Sie den Namen direkt ein."
)