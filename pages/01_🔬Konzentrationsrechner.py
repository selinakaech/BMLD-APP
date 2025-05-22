# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st

def set_background_with_transparency():
    st.markdown("""
    <style>
    /* Bild auf HTML und Body anwenden */
    html, body {
        background: url("https://images.pexels.com/photos/7722796/pexels-photo-7722796.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2") no-repeat center center fixed;
        background-size: cover;
    }

    /* Overlay über das Haupt-Container-Element */
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255,255,255,0.92);  /* Bild nur noch sehr schwach sichtbar */
        z-index: 0;
        pointer-events: none;
    }

    /* Inhalt über dem Overlay sichtbar */
    .stApp {
        position: relative;
        z-index: 1;
    }

    /* Optional: Textlesbarkeit */
    h1, h2, h3, h4, h5, p, label {
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
    }

    /* Optional: Heller Bereich */
    section.main > div {
        background-color: rgba(255,255,255,0.85);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Hintergrundbild mit Transparenz setzen
set_background_with_transparency()



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