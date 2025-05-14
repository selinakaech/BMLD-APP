import streamlit as st
import random
import matplotlib.pyplot as plt
 
# Definiere die Liste von Beispiel-Fragen und Antworten
questions = [
    {"question": "Was ist der pKs-Wert von HCl?", "answer": "-6"},
    {"question": "Welches Symbol hat das Element mit der Ordnungszahl 1?", "answer": "H"},
    {"question": "Was ist die molare Masse von Wasser (H2O)?", "answer": "18.015"},
    {"question": "Welche Elektronegativität hat Chlor?", "answer": "3.16"},
    {"question": "Was ist der Aggregatzustand von Wasser bei Raumtemperatur?", "answer": "flüssig"},
    {"question": "Welche Dichte hat Gold?", "answer": "19.32"},
    {"question": "Was ist die pKs-Wert von Essigsäure?", "answer": "4.72"},
    {"question": "Was ist die Ordnungszahl von Sauerstoff?", "answer": "8"},
    {"question": "Was ist der pKs-Wert von Schwefelsäure?", "answer": "-3"},
    {"question": "Wie viele Protonen hat ein Wasserstoffatom?", "answer": "1"},
    {"question": "Was ist die Kategorie von Kohlenstoff?", "answer": "Nichtmetall"},
    {"question": "Was ist die Erscheinung von Gold?", "answer": "gelb, glänzend"},
    {"question": "Was ist der pKs-Wert von HNO3?", "answer": "-1.32"},
    {"question": "Was ist die Elektronegativität von Fluor?", "answer": "3.98"},
    {"question": "Welche Dichte hat Eisen?", "answer": "7.87"},
    {"question": "Was ist die molare Masse von Helium?", "answer": "4.0026"},
    {"question": "Was ist der pKs-Wert von Oxalsäure?", "answer": "1.46"},
    {"question": "Was ist der Aggregatzustand von Sauerstoff bei Raumtemperatur?", "answer": "gasförmig"},
    {"question": "Was ist der pKs-Wert von Ammonium?", "answer": "9.21"},
    {"question": "Was ist der pKs-Wert von Acetat?", "answer": "4.72"},
    {"question": "Was ist die Ordnungszahl von Kohlenstoff?", "answer": "6"},
    {"question": "Was ist der pKs-Wert von Natriumhydroxid?", "answer": "13.0"},
    {"question": "Welche Dichte hat Kupfer?", "answer": "8.96"},
    {"question": "Was ist der Aggregatzustand von Methan bei Raumtemperatur?", "answer": "gasförmig"},
    {"question": "Was ist der pKs-Wert von Hydroxid?", "answer": "15.74"},
    {"question": "Was ist der pKs-Wert von Schwefelwasserstoff?", "answer": "7.06"},
    {"question": "Was ist die Elektronegativität von Sauerstoff?", "answer": "3.44"},
    {"question": "Was ist die Dichte von Wasser?", "answer": "1.00"},
    {"question": "Was ist der pKs-Wert von Phosphorsäure?", "answer": "1.96"},
    {"question": "Was ist der pKs-Wert von Hydrofluorsäure?", "answer": "3.14"}
]
 
# Definiere den Lernfortschritt
progress = {
    "correct_answers": 0,
    "total_answers": 0
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
 
# Quiz-Seite
def quiz_page():
    # Auswahl von 3 zufälligen Fragen
    random_questions = random.sample(questions, 3)
    st.title("📝 Quiz")
    st.write("Beantworten Sie bitte die folgenden Fragen:")
    answers = {}
    for i, q in enumerate(random_questions, start=1):
        st.text(f"{i}. {q['question']}")
        answer = st.text_input(f"Antwort für Frage {i}", key=f"answer_{i}")
        answers[i] = answer
 
    if st.button("Antworten abschicken"):
        # Überprüfen der Antworten
        for i, q in enumerate(random_questions, start=1):
            correct = "Richtig" if answers[i].lower() == q["answer"].lower() else "Falsch"
            st.write(f"Frage {i}: {correct} (Ihre Antwort: {answers[i]})")
 
            if correct == "Richtig":
                progress["correct_answers"] += 1
            progress["total_answers"] += 1
        st.success("Antworten gespeichert (Demo)")
        st.write("Jetzt können Sie den Lernfortschritt auf der nächsten Seite sehen.")
        # Weiterleitung zur Lernfortschritts-Seite
        if st.button("Zum Lernfortschritt"):
            st.session_state["current_page"] = "Lernfortschritt"
 
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