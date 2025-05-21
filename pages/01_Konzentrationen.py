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
image_url = "https://images.pexels.com/photos/2280549/pexels-photo-2280549.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
 
# Hintergrund setzen
set_background_from_url(image_url)

# Titel und Einführung mit Emoji
st.title("🔬 Konzentrationsrechner")

st.write(
    "Willkommen beim **Konzentrationsrechner**! Berechne die Konzentration einer Lösung "
    "mit Hilfe der Stoffmenge und des Volumens. Gib einfach die Werte ein und erhalte das Ergebnis! ✨"
)

# Eingabefelder in einem ansprechenden Layout
col1, col2 = st.columns(2)

with col1:
    n = st.number_input("⚗️ Stoffmenge (mol)", min_value=0.0, step=0.01, help="Geben Sie die Stoffmenge in Mol ein.")

with col2:
    V = st.number_input("🌡️ Volumen (L)", min_value=0.0, step=0.01, help="Geben Sie das Volumen in Litern ein.")

# Berechnung und Ausgabe im Resultate-Fenster
if n > 0 and V > 0:
    c = n / V
    st.success(f"🎉 **Ergebnis**: Die Konzentration beträgt: **{c:.2f} mol/L**")

    # Ergebnis-Details in einem "Resultate"-Fenster
    with st.expander("📊 Resultate Details"):
        st.write(f"**Stoffmenge (n):** {n} mol")
        st.write(f"**Volumen (V):** {V} L")
        st.write(f"**Konzentration (c):** {c:.2f} mol/L")
else:
    st.error("❗ Bitte stellen Sie sicher, dass sowohl die Stoffmenge als auch das Volumen grösser als 0 sind.")

# Zusätzliche Tipps in einem Info-Fenster
st.info(
    "ℹ️ Tipp: Um die Konzentration in anderen Einheiten zu berechnen, passen Sie einfach die Eingabewerte an."
)