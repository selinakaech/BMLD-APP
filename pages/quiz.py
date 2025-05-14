import streamlit as st
import random
import matplotlib.pyplot as plt
import pandas as pd
 
# Liste von 15 statischen Fragen und Antworten
questions = [
    {"question": "Was ist die chemische Formel von Wasser?", "answer": "H2O"},
    {"question": "Welches Element hat das Symbol H?", "answer": "Wasserstoff"},
    {"question": "Welches Element hat das Symbol O?", "answer": "Sauerstoff"},
    {"question": "Wie viele Protonen hat ein Wasserstoffatom?", "answer": "1"},
    {"question": "Welches Gas atmen Menschen ein?", "answer": "Sauerstoff"},
    {"question": "Was ist der pH-Wert von reinem Wasser?", "answer": "7"},
    {"question": "Welches Element hat das Symbol Na?", "answer": "Natrium"},
    {"question": "Was ist der Aggregatzustand von Eis bei Raumtemperatur?", "answer": "fest"},
    {"question": "Was ist der Aggregatzustand von Sauerstoff bei Raumtemperatur?", "answer": "gasförmig"},
    {"question": "Wie viele Elemente gibt es im Periodensystem?", "answer": "118"},
    {"question": "Was ist die chemische Formel von Salz?", "answer": "NaCl"},
    {"question": "Wie nennt man das Element mit der Ordnungszahl 1?", "answer": "Wasserstoff"},
    {"question": "Was ist der pKs-Wert von Salzsäure?", "answer": "-6"},
    {"question": "Was ist die Farbe von Kupfer?", "answer": "rotbraun"},
    {"question": "Welches Element hat das Symbol He?", "answer": "Helium"}
]
 
# Definiere den Lernfortschritt
progress = {
    "correct_answers": 0,
    "total_answers": 0,
    "answers_detail": [],  # Speichert Details zu jeder Antwort
    "time_steps": [],  # Speichert Fortschritt bei jedem Schritt
}
 
# Funktion für den Fortschritts-Chart
def plot_progress(correct_answers, total_answers):
    # Berechnung des Fortschritts
    progress_percentage = (correct_answers / total_answers) * 100 if total_answers > 0 else 0
    fig, ax = plt.subplots()
    ax.bar(["Fortschritt"], [progress_percentage], color='green')
    ax.set_ylim(0, 100)
    ax.set_ylabel("Fortschritt (%)")
    ax.set_title("Lernfortschritt")
    st.pyplot(fig)
 
# Funktion zur Darstellung des Lernfortschritts im Verlauf der Zeit
def plot_time_series(progress_data):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(range(1, len(progress_data) + 1), progress_data, marker='o', color='blue', linestyle='-', linewidth=2)
    ax.set_xlabel('Fragen')
    ax.set_ylabel('Fortschritt (%)')
    ax.set_title('Lernfortschritt im Verlauf des Quiz')
    ax.set_ylim(0, 100)
    st.pyplot(fig)
 
# Quiz-Seite
def quiz_page():
    st.title("📝 Quiz")
    answers = {}
    progress_data = []
 
    # Iteriere durch alle Fragen und stelle sie der Reihe nach
    for i, q in enumerate(questions, start=1):
        st.text(f"{i}. {q['question']}")
        answer = st.text_input(f"Antwort für Frage {i}", key=f"answer_{i}")
        answers[i] = answer
        # Zeige den aktuellen Fortschritt nach jeder Frage
        if st.button(f"Antworten nach Frage {i} abschicken"):
            correct = "Richtig" if answers[i].lower() == q["answer"].lower() else "Falsch"
            st.write(f"Frage {i}: {correct} (Ihre Antwort: {answers[i]})")
 
            # Fortschritt speichern
            if correct == "Richtig":
                progress["correct_answers"] += 1
            progress["total_answers"] += 1
 
            # Fortschritt bei diesem Schritt speichern
            progress_percentage = (progress["correct_answers"] / progress["total_answers"]) * 100 if progress["total_answers"] > 0 else 0
            progress_data.append(progress_percentage)
            # Speichern der Antwortdetails (Frage, Antwort und Status)
            progress["answers_detail"].append({
                "Frage": q["question"],
                "Ihre Antwort": answers[i],
                "Status": correct
            })
    # Zeige den Gesamtfortschritt nach der letzten Frage
    if st.button("Antworten abschicken und Fortschritt anzeigen"):
        st.success("Antworten gespeichert (Demo)")
        plot_progress(progress["correct_answers"], progress["total_answers"])
 
        # Zeitliche Darstellung des Fortschritts
        plot_time_series(progress_data)
        # Tabelle mit Antworten und Status anzeigen
        st.subheader("Antworten im Detail:")
        answers_df = pd.DataFrame(progress["answers_detail"])
        st.dataframe(answers_df)
 
        # Button zum Wiederholen des Quiz
        if st.button("Quiz wiederholen"):
            # Reset für die aktuellen Fortschrittsdaten und Umleitung zur Quiz-Seite
            progress["correct_answers"] = 0
            progress["total_answers"] = 0
            progress["answers_detail"] = []
            progress["time_steps"] = []
            st.session_state["current_page"] = "Quiz"
            st.experimental_rerun()
 
# App-Logik
def app():
    # Überprüfen, ob der Benutzer bereits eine Seite ausgewählt hat
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Quiz"
    if st.session_state["current_page"] == "Quiz":
        quiz_page()
 
# Seitenaufruf starten
if __name__ == "__main__":
    app()