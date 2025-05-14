import streamlit as st

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

    "answers_detail": []  # Speichert Details zu jeder Antwort

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

    st.title("📝 Quiz")
 
    answers = {}

    # Iteriere durch alle Fragen

    for i, q in enumerate(questions, start=1):

        st.text(f"{i}. {q['question']}")

        answer = st.text_input(f"Antwort für Frage {i}", key=f"answer_{i}")

        answers[i] = answer
 
    # Button, um alle Antworten zu überprüfen und den Fortschritt zu berechnen

    if st.button("Antworten abschicken"):

        # Überprüfen der Antworten und speichern der Details

        for i, q in enumerate(questions, start=1):

            correct = "Richtig" if answers[i].lower() == q["answer"].lower() else "Falsch"

            st.write(f"Frage {i}: {correct} (Ihre Antwort: {answers[i]})")
 
            if correct == "Richtig":

                progress["correct_answers"] += 1

            progress["total_answers"] += 1
 
            # Speichern der Antwortdetails (Frage, Antwort und Status)

            progress["answers_detail"].append({

                "Frage": q["question"],

                "Ihre Antwort": answers[i],

                "Status": correct

            })

        st.success("Antworten gespeichert (Demo)")

        st.write("Jetzt können Sie den Lernfortschritt unten sehen.")

        # Lernfortschritt anzeigen

        plot_progress(progress["correct_answers"], progress["total_answers"])
 
        # Tabelle mit Antworten und Status anzeigen

        st.subheader("Antworten im Detail:")

        answers_df = pd.DataFrame(progress["answers_detail"])

        st.dataframe(answers_df)
 
# App-Logik

def app():

    # Quiz-Seite aufrufen

    quiz_page()
 
# Seitenaufruf starten

if __name__ == "__main__":

    app()

 