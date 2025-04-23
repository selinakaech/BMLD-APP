import streamlit as st

from utils.login_manager import LoginManager
 
def app():

    # Login immer **innerhalb** der Funktion, nicht davor

    try:

        LoginManager().go_to_login('Start.py')

    except Exception as e:

        st.error(f"🔒 Fehler im Login-Block: {e}")

        return
 
    st.title("Konzentration berechnen")

    n = st.number_input("Stoffmenge (mol)")

    V = st.number_input("Volumen (L)")

    if n and V:

        c = n / V

        st.write(f"Konzentration: {c:.2f} mol/L")

 