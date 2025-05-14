import streamlit as st
import pandas as pd
from quiz import quiz   # Importiere die Quiz-Funktion

# Lernfortschritt-Seite
def progress_page():
    st.title("📈 Lernfortschritt")
    # Anzeige des Lernfortschritts in einem Diagramm
    plot_progress(progress["correct_answers"], progress["total_answers"])
 
    # Anzeige einer Tabelle mit den Antworten und deren Status
    if progress["total_answers"] > 0:
        st.subheader("Antworten im Detail:")
        answers_df = pd.DataFrame(progress["answers_detail"])
        st.dataframe(answers_df)
 
# App-Logik
def app():
    # Überprüfen, ob der Benutzer bereits eine Seite ausgewählt hat
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Quiz"
    if st.session_state["current_page"] == "Quiz":
        quiz_page()
    elif st.session_state["current_page"] == "Lernfortschritt":
        progress_page()