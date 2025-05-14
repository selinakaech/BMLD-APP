import streamlit as st
 
# Globale Einstellungen laden
if 'background_color' not in st.session_state:
    st.session_state['background_color'] = '#ffffff'
if 'font' not in st.session_state:
    st.session_state['font'] = 'Arial'
if 'animation' not in st.session_state:
    st.session_state['animation'] = 'Kein Effekt'
 
# Einstellungsseite
def einstellungen():
    st.title("🎨 Personalisierung der App")
    st.write("Wähle deine persönlichen Einstellungen aus.")
 
    with st.form("settings_form"):
        # Hintergrundfarbe
        bg_color = st.color_picker("Hintergrundfarbe", st.session_state['background_color'])
        font = st.selectbox("Schriftart", ["Arial", "Courier New", "Verdana", "Times New Roman", "Georgia"], index=["Arial", "Courier New", "Verdana", "Times New Roman", "Georgia"].index(st.session_state['font']))
        animation = st.selectbox("Animationseffekt", ["Kein Effekt", "Feuerwerk", "Schneefall", "Regen"], index=["Kein Effekt", "Feuerwerk", "Schneefall", "Regen"].index(st.session_state['animation']))
 
        submit = st.form_submit_button("Speichern")
 
    if submit:
        st.session_state['background_color'] = bg_color
        st.session_state['font'] = font
        st.session_state['animation'] = animation
        st.success("Einstellungen gespeichert!")
 
# Anwenden der globalen Einstellungen
st.markdown(f"<style>body {{ background-color: {st.session_state['background_color']}; font-family: {st.session_state['font']}; }}</style>", unsafe_allow_html=True)
 
# Animationseffekt
if st.session_state['animation'] == 'Feuerwerk':
    st.balloons()
elif st.session_state['animation'] == 'Schneefall':
    st.snow()
 
# Hauptaufruf der Einstellungsseite
einstellungen()