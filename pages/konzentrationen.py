import streamlit as st

# Anwenden der globalen Einstellungen
if 'background_color' in st.session_state and 'font' in st.session_state:
    st.markdown(f"<style>body {{ background-color: {st.session_state['background_color']}; font-family: {st.session_state['font']}; }}</style>", unsafe_allow_html=True)
 
# Animationseffekt
if 'animation' in st.session_state:
    if st.session_state['animation'] == 'Feuerwerk':
        st.balloons()
    elif st.session_state['animation'] == 'Schneefall':
        st.snow()
 
def app():

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

        st.error("❗ Bitte stellen Sie sicher, dass sowohl die Stoffmenge als auch das Volumen größer als 0 sind.")

    # Zusätzliche Tipps in einem Info-Fenster

    st.info(

        "ℹ️ Tipp: Um die Konzentration in anderen Einheiten zu berechnen, passen Sie einfach die Eingabewerte an."

    )

 