import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.radio("Gehe zu", [
    "Startseite", 
    "Hauptseite", 
    "Periodensystem", 
    "Massenrechner", 
    "pH-Rechner", 
    "Säure-Base-Tabelle", 
    "Konzentration berechnen", 
    "Quiz", 
    "Lösungen", 
    "Settings"
])