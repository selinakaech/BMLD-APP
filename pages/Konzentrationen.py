import streamlit as st
 
def app():
    if not st.session_state.logged_in:
        st.warning("Du musst dich zuerst einloggen!")
        return
 
    # Berechnung der Konzentration
    st.title("Konzentration berechnen")
    n = st.number_input("Stoffmenge (mol)")
    V = st.number_input("Volumen (L)")
    if n and V:
        c = n / V
        st.write(f"Konzentration: {c:.2f} mol/L")