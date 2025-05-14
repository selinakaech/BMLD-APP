import streamlit as st
import pandas as pd
 
# Definiere die app()-Funktion
def app():
    # Titel und Einführung mit Emoji
    st.title("⚗️ Säure-Base-Tabelle")
    st.write(
        "Berechne und betrachte die **pKs-Werte** von Säuren und Basen. "
        "Geben Sie einfach den Namen einer Säure oder Base ein und erfahren Sie den zugehörigen pKs-Wert. 🔬"
    )
    # Eingabefelder für Säure und Base
    saure = st.text_input("🔴 Geben Sie eine Säure ein (z.B. HCl)")
    base = st.text_input("🔵 Geben Sie eine Base ein (z.B. NaOH)")
    # Tabelle mit pKs-Werten für gängige Säuren und Basen
    pKs_wert = {
        "HCl":  -6.3,
        "H₂SO₄": -3.0,
        "CH₃COOH": 4.76,
        "NH₃":  9.25,
        "NaOH": 13.0,
        "KOH": 13.0
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