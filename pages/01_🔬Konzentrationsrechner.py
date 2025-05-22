# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st

# Funktion, um den Hintergrund per Bild-URL zu setzen
def set_background_from_url(image_url): 
    st.markdown(
        f"""
<style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), 
                              url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
</style>
        """,
        unsafe_allow_html=True
    )
 
# Deine Bild-URL
image_url = "https://images.pexels.com/photos/7722796/pexels-photo-7722796.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
 
# Hintergrund setzen
set_background_from_url(image_url)



# Titel und Einführung mit Emoji
st.title("🔬 Konzentrationsrechner")
 
st.write(
    "Willkommen beim **Konzentrationsrechner**! Gib zwei beliebige Werte ein – "
    "**Stoffmenge (n)**, **Volumen (V)** oder **Konzentration (c)** – "
    "und der fehlende Wert wird automatisch berechnet. ⚗️"
)
 
# Eingabefelder mit None als Platzhalter für leere Eingaben
st.markdown("### 🔢 Eingabe der bekannten Werte:")
 
col1, col2, col3 = st.columns(3)
 
with col1:
    n_input = st.text_input("⚗️ Stoffmenge (mol)", help="z. B. 0.5")
 
with col2:
    V_input = st.text_input("🌡️ Volumen (L)", help="z. B. 1.0")
 
with col3:
    c_input = st.text_input("🧪 Konzentration (mol/L)", help="z. B. 0.5")
 
# Umwandlung von Eingaben in float (falls vorhanden)
def to_float(val):
    try:
        return float(val)
    except:
        return None
 
n = to_float(n_input)
V = to_float(V_input)
c = to_float(c_input)
 
# Berechnungslogik
if n is not None and V is not None and c is None:
    c = n / V
    fehlend = "Konzentration"
    einheit = "mol/L"
elif n is not None and c is not None and V is None:
    V = n / c
    fehlend = "Volumen"
    einheit = "L"
elif V is not None and c is not None and n is None:
    n = c * V
    fehlend = "Stoffmenge"
    einheit = "mol"
else:
    fehlend = None
 
# Ergebnisanzeige
if fehlend:
    fehlend_map = {
        "Konzentration": c,
        "Volumen": V,
        "Stoffmenge": n
    }
    st.success(f"🎉 **Ergebnis**: Die berechnete {fehlend} beträgt **{fehlend_map[fehlend]:.3f} {einheit}**")
    with st.expander("📊 Resultate Details"):
        st.write(f"**Stoffmenge (n):** {n:.3f} mol")
        st.write(f"**Volumen (V):** {V:.3f} L")
        st.write(f"**Konzentration (c):** {c:.3f} mol/L")
elif all(x is not None for x in [n, V, c]):
    st.warning("⚠️ Bitte geben Sie **nur zwei** Werte ein, damit der dritte berechnet werden kann.")
elif sum(x is not None for x in [n, V, c]) < 2:
    st.info("ℹ️ Bitte geben Sie **zwei Werte** ein, um den dritten zu berechnen.")