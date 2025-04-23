import streamlit as st
from utils.login_manager import LoginManager
 
def app():
    LoginManager().go_to_login('Start.py')  # Jetzt wird das nur ausgeführt, wenn app() aufgerufen wird
 
    st.title("Konzentration berechnen")
    n = st.number_input("Stoffmenge (mol)")
    V = st.number_input("Volumen (L)")
    if n and V:
        c = n / V
        st.write(f"Konzentration: {c:.2f} mol/L")