import streamlit as st
 
def app():
    # Titel und Einleitung
    st.title("Konzentrationsrechner")
    st.write(
        "Willkommen beim Konzentrationsrechner! Berechne die Konzentration einer Lösung "
        "mit Hilfe der Stoffmenge und des Volumens."
    )
    # Eingabefelder in einem ansprechenden Layout
    col1, col2 = st.columns(2)
    with col1:
        n = st.number_input("Stoffmenge (mol)", min_value=0.0, step=0.01, help="Geben Sie die Stoffmenge in Mol ein.")
    with col2:
        V = st.number_input("Volumen (L)", min_value=0.0, step=0.01, help="Geben Sie das Volumen in Litern ein.")
    # Berechnung und Ausgabe
    if n > 0 and V > 0:
        c = n / V
        st.success(f"Die Konzentration beträgt: **{c:.2f} mol/L**")
    else:
        st.error("Bitte stellen Sie sicher, dass sowohl die Stoffmenge als auch das Volumen größer als 0 sind.")
    # Zusätzliche Information oder Tipps
    st.info(
        "Tipp: Um die Konzentration in anderen Einheiten zu berechnen, passen Sie einfach die Eingabewerte an."
    )