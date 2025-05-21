# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
 
# Definiere die app()-Funktion
def app():
    # Titel und Einführung mit Emoji
    st.title("⚖️ Massenrechner")
    st.write(
        "Berechne die **Stoffmenge** aus der **Masse** und der **Molmasse**. "
        "Gib die Masse der Substanz und ihre Molmasse ein, um die Stoffmenge in Mol zu berechnen. 🔬"
    )
    # Eingabefelder in einem ansprechenden Layout
    col1, col2 = st.columns(2)
    with col1:
        masse = st.number_input("Masse (g)", min_value=0.0, step=0.01, help="Geben Sie die Masse der Substanz in Gramm ein.")
    with col2:
        molare_masse = st.number_input("Molmasse (g/mol)", min_value=0.0, step=0.01, help="Geben Sie die Molmasse der Substanz in g/mol ein.")
    # Berechnung und Ausgabe im Resultate-Fenster
    if masse > 0 and molare_masse > 0:
        stoffmenge = masse / molare_masse
        st.success(f"🎉 **Ergebnis**: Die Stoffmenge beträgt: **{stoffmenge:.3f} mol**")
        # Ergebnis-Details in einem "Resultate"-Fenster
        with st.expander("📊 Resultate Details"):
            st.write(f"**Masse (m):** {masse} g")
            st.write(f"**Molmasse (M):** {molare_masse} g/mol")
            st.write(f"**Stoffmenge (n):** {stoffmenge:.3f} mol")
    else:
        st.error("❗ Bitte stellen Sie sicher, dass sowohl die Masse als auch die Molmasse größer als 0 sind.")
    # Zusätzliche Tipps in einem Info-Fenster
    st.info(
        "ℹ️ Tipp: Wenn Sie die Masse oder Molmasse einer anderen Substanz berechnen möchten, passen Sie einfach die Eingabewerte an."
    )