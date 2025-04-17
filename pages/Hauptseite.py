import streamlit as st

# Initialisierung
if "page" not in st.session_state:
    st.session_state.page = "Startseite"

# Funktion zur Navigation
def switch_page(new_page):
    st.session_state.page = new_page

# Seitenlogik
if st.session_state.page == "Startseite":
    st.title("Herzlich Willkommen bei...")
    st.text_input("Username", key="user")
    st.text_input("Passwort", type="password", key="pass")
    if st.button("Login"):
        switch_page("Hauptseite")

elif st.session_state.page == "Hauptseite":
    st.title("Name der App")
    st.write("Willkommen! Wähle eine Funktion:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Periodensystem"):
            switch_page("Periodensystem")
        if st.button("pH-Rechner"):
            switch_page("pH-Rechner")
        if st.button("Konzentration"):
            switch_page("Konzentration")
    with col2:
        if st.button("Massenrechner"):
            switch_page("Massenrechner")
        if st.button("Säure-Base-Tabelle"):
            switch_page("Säure-Base-Tabelle")
        if st.button("Quiz"):
            switch_page("Quiz")

elif st.session_state.page == "Periodensystem":
    st.title("Periodensystem")
    st.write("Element eingeben:")
    st.text_input("Element")
    if st.button("Zurück"):
        switch_page("Hauptseite")

elif st.session_state.page == "Massenrechner":
    st.title("Massenrechner")
    masse = st.number_input("Masse (g)")
    molare_masse = st.number_input("Molmasse (g/mol)")
    if molare_masse:
        n = masse / molare_masse
        st.write(f"Stoffmenge: {n:.3f} mol")
    if st.button("Zurück"):
        switch_page("Hauptseite")

elif st.session_state.page == "pH-Rechner":
    st.title("pH-Rechner")
    import math
    c_h3o = st.number_input("Konzentration [H₃O⁺] in mol/L")
    if c_h3o > 0:
        ph = -math.log10(c_h3o)
        st.write(f"pH-Wert: {ph:.2f}")
    if st.button("Zurück"):
        switch_page("Hauptseite")

elif st.session_state.page == "Säure-Base-Tabelle":
    st.title("Säure-Base-Tabelle")
    st.text_input("Säure:")
    st.text_input("Base:")
    if st.button("Zurück"):
        switch_page("Hauptseite")

elif st.session_state.page == "Konzentration":
    st.title("Konzentration berechnen")
    n = st.number_input("Stoffmenge (mol)")
    V = st.number_input("Volumen (L)")
    if V:
        c = n / V
        st.write(f"Konzentration: {c:.2f} mol/L")
    if st.button("Zurück"):
        switch_page("Hauptseite")

elif st.session_state.page == "Quiz":
    st.title("Quiz")
    st.write("1. Was ist der pH-Wert von Wasser?")
    st.write("2. Welche Einheit hat die Konzentration?")
    st.write("3. Wie viele Protonen hat Sauerstoff?")
    if st.button("Antworten abschicken"):
        st.success("Antworten gespeichert (Demo)")
    if st.button("Zurück"):
        switch_page("Hauptseite")