import streamlit as st

# Periodensystem (Platzhalter)
elif page == "Periodensystem":
    st.title("Periodensystem")
    st.write("Geben Sie ein Element ein:")
    element = st.text_input("Element")
    if element:
        st.write(f"Informationen zu: {element}")
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large_de.png", use_column_width=True)