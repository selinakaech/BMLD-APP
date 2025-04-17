# Säure-Base-Tabelle
elif page == "Säure-Base-Tabelle":
    st.title("Säure-Base-Tabelle")
    saure = st.text_input("Geben Sie eine Säure ein")
    base = st.text_input("Geben Sie eine Base ein")
    if saure or base:
        st.write(f"pKs-Wert (Demo): 4.75")