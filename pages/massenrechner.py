import streamlit as st

# Definiere die app()-Funktion
def app():
    # Massenrechner
    st.title("Massenrechner")
    masse = st.number_input("Masse (g)")
    molare_masse = st.number_input("Molmasse (g/mol)")
    if masse and molare_masse:
        stoffmenge = masse / molare_masse
        st.write(f"Stoffmenge: {stoffmenge:.3f} mol")