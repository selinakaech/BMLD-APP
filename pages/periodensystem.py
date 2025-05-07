import streamlit as st

# Datenbank der Elementeigenschaften
ELEMENT_DATA = {
    "H": {
        "name": "Wasserstoff",
        "molmasse": 1.008,
        "elektronegativität": 2.20,
        "aggregatzustand": "gasförmig",
        "dichte": 0.00008988,  # g/cm³
        "ordnungszahl": 1,
        "bild": "https://upload.wikimedia.org/wikipedia/commons/8/80/Hydrogen_Spectra.jpg"
    },
    "O": {
        "name": "Sauerstoff",
        "molmasse": 15.999,
        "elektronegativität": 3.44,
        "aggregatzustand": "gasförmig",
        "dichte": 0.001429,  # g/cm³
        "ordnungszahl": 8,
        "bild": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Oxygen_discharge_tube.jpg"
    },
    "Fe": {
        "name": "Eisen",
        "molmasse": 55.845,
        "elektronegativität": 1.83,
        "aggregatzustand": "fest",
        "dichte": 7.874,  # g/cm³
        "ordnungszahl": 26,
        "bild": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Iron_electrolytic_and_1cm3_cube.jpg"
    },
    # Weitere Elemente können hier hinzugefügt werden...
}

# Definiere die app()-Funktion
def app():
    # Periodensystem
    st.title("Periodensystem")
    st.write("Geben Sie ein Elementsymbol ein (z. B. H, O, Fe):")
    element = st.text_input("Element").capitalize()

    if element in ELEMENT_DATA:
        data = ELEMENT_DATA[element]
        st.subheader(f"Informationen zu {data['name']} ({element})")
        st.write(f"**Molmasse:** {data['molmasse']} g/mol")
        st.write(f"**Elektronegativität:** {data['elektronegativität']}")
        st.write(f"**Aggregatzustand:** {data['aggregatzustand']}")
        st.write(f"**Dichte:** {data['dichte']} g/cm³")
        st.write(f"**Ordnungszahl:** {data['ordnungszahl']}")
        st.image(data["bild"], caption=f"{data['name']} ({element})", use_container_width=True)
    elif element:
        st.error("Das eingegebene Element wurde nicht gefunden. Bitte überprüfen Sie das Symbol.")
    else:
        st.info("Bitte geben Sie ein Elementsymbol ein, um Informationen anzuzeigen.")