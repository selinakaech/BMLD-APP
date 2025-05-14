# Lernfortschritt-Seite
def progress_page():
    st.title("📈 Lernfortschritt")
    plot_progress(progress["correct_answers"], progress["total_answers"])
 
# App-Logik
def app():
    # Überprüfen, ob der Benutzer bereits eine Seite ausgewählt hat
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Quiz"
    if st.session_state["current_page"] == "Quiz":
        quiz_page()
    elif st.session_state["current_page"] == "Lernfortschritt":
        progress_page()