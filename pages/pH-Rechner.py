# pH-Rechner
elif page == "pH-Rechner":
    st.title("pH-Rechner")
    c_h3o = st.number_input("Konzentration [H₃O⁺] in mol/L")
    if c_h3o > 0:
        ph = -math.log10(c_h3o)
        st.write(f"pH-Wert: {ph:.2f}")