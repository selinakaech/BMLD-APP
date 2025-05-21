# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import math

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
image_url = "https://s.zentrum-der-gesundheit.de/img/ph-wert"
 
# Hintergrund setzen
set_background_from_url(image_url)

# pH-Rechner Titel und Einführung mit Emoji
st.title("🧪 pH-Rechner")

st.write(
    "Berechne den **pH-Wert** einer Lösung basierend auf der **Konzentration von H₃O⁺**. "
    "Gib einfach die Konzentration von H₃O⁺ in mol/L ein und erhalte den pH-Wert. 🔬"
)

# Eingabefeld für die Konzentration in einem ansprechenden Layout
c_h3o = st.number_input(
    "Konzentration [H₃O⁺] in mol/L", 
    min_value=0.0, 
    step=0.0001, 
    help="Geben Sie die Konzentration von H₃O⁺ in mol/L ein."
)

# Berechnung und Ausgabe im Resultate-Fenster
if c_h3o > 0:
    ph = -math.log10(c_h3o)
    st.success(f"🎉 **Ergebnis**: Der pH-Wert der Lösung beträgt: **{ph:.2f}**")
    with st.expander("📊 Resultate Details"):
        st.write(f"**Konzentration [H₃O⁺]:** {c_h3o} mol/L")
        st.write(f"**Berechneter pH-Wert:** {ph:.2f}")
elif c_h3o == 0:
    st.info("Bitte geben Sie eine Konzentration grösser als 0 ein.")