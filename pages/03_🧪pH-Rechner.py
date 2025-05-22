# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import math
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
image_url = "https://s.zentrum-der-gesundheit.de/img/ph-wert"
 
# Hintergrund setzen
set_background_from_url(image_url)

# pH-Rechner Titel und Einführung mit Emoji
import streamlit as st

import math
 
st.title("🧪 pH-Rechner")
 
st.write(

    "Berechne entweder den **pH-Wert** aus der **H₃O⁺-Konzentration**, "

    "oder umgekehrt die Konzentration aus einem gegebenen pH-Wert. "

    "Gib einfach einen der beiden Werte ein! 🔄"

)
 
# Eingabefelder

col1, col2 = st.columns(2)
 
with col1:

    c_h3o_input = st.text_input("🔬 Konzentration [H₃O⁺] (mol/L)", help="z. B. 0.001")
 
with col2:

    ph_input = st.text_input("🧪 pH-Wert", help="z. B. 3.0")
 
# Umwandlung in float

def to_float(value):

    try:

        return float(value)

    except:

        return None
 
c_h3o = to_float(c_h3o_input)

ph = to_float(ph_input)
 
# Berechnung

if c_h3o is not None and ph is None:

    if c_h3o > 0:
        ph = -math.log10(c_h3o)
        st.success(f"✅ Der berechnete **pH-Wert** beträgt: **{ph:.2f}**")
        with st.expander("📊 Details"):
            st.write(f"**Eingegebene Konzentration [H₃O⁺]:** {c_h3o:.4e} mol/L")
            st.write(f"**Berechneter pH-Wert:** {ph:.2f}")
    elif c_h3o == 0:
        st.info("ℹ️ Eine Konzentration von 0 mol/L bedeutet, dass keine H₃O⁺-Ionen vorhanden sind. Der pH-Wert ist in diesem Fall nicht definiert.")
elif ph is not None and c_h3o is None:
    if ph >= 0:
        c_h3o = 10 ** (-ph)

        st.success(f"✅ Die berechnete **[H₃O⁺]-Konzentration** beträgt: **{c_h3o:.4e} mol/L**")

        with st.expander("📊 Details"):
            st.write(f"**Eingegebener pH-Wert:** {ph:.2f}")
            st.write(f"**Berechnete Konzentration [H₃O⁺]:** {c_h3o:.4e} mol/L")
    else:
        st.error("❗ Der pH-Wert muss ≥ 0 sein.")
elif ph is not None and c_h3o is not None:
    st.warning("⚠️ Bitte geben Sie **nur einen** der beiden Werte ein – entweder den pH-Wert oder die H₃O⁺-Konzentration.")
else:
    st.info("ℹ️ Bitte geben Sie entweder den **pH-Wert** oder die **[H₃O⁺]-Konzentration** ein.")

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