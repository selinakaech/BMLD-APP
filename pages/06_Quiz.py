# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import random
import pandas as pd

# Funktion, um den Hintergrund per Bild-URL zu setzen
def set_background_from_url(image_url): 
    st.markdown(
        f"""
<style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
</style>
        """,
        unsafe_allow_html=True
    )
 
# Deine Bild-URL
image_url = ""
 
# Hintergrund setzen
set_background_from_url(image_url)

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
    "answers_detail": [],
    "time_steps": [],
}

def quiz_page():
    st.title("📝 Quiz")

    answers = {}
    progress_data = []

    for i, q in enumerate(questions, start=1):
        st.text(f"{i}. {q['question']}")
        answer = st.text_input(f"Antwort für Frage {i}", key=f"answer_{i}")
        answers[i] = answer

    if st.button("Antworten abschicken"):
        for i, q in enumerate(questions, start=1):
            correct = "Richtig" if answers[i].lower() == q["answer"].lower() else "Falsch"
            st.write(f"Frage {i}: {correct} (Ihre Antwort: {answers[i]})")

            if correct == "Richtig":
                progress["correct_answers"] += 1
            progress["total_answers"] += 1

            progress_percentage = (progress["correct_answers"] / progress["total_answers"]) * 100 if progress["total_answers"] > 0 else 0
            progress_data.append(progress_percentage)
            progress["answers_detail"].append({
                "Frage": q["question"],
                "Ihre Antwort": answers[i],
                "Status": correct
            })

        result = {
            "correct_answers": progress["correct_answers"],
            "total_answers": progress["total_answers"],
            "answers_detail": progress["answers_detail"],
        }
        from utils.data_manager import DataManager
        DataManager().append_record(session_state_key='data_df', record_dict=result)

        # Session State direkt aktualisieren (Lösung)
        # Nur einfache Werte für den Lernfortschritt speichern!
        result_simple = {
            "correct_answers": progress["correct_answers"],
            "total_answers": progress["total_answers"],
            "timestamp": pd.Timestamp.now()
        }
        if 'data_df' in st.session_state and not st.session_state['data_df'].empty:
            st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([result_simple])], ignore_index=True)
        else:
            st.session_state['data_df'] = pd.DataFrame([result_simple])

        st.success("Antworten gespeichert (Demo)")
        st.write("Jetzt können Sie Ihre persönliche Entwicklung unter Lernfortschritt anzeigen lassen.")

        st.subheader("Antworten im Detail:")
        answers_df = pd.DataFrame(progress["answers_detail"])
        st.dataframe(answers_df)

        if st.button("Quiz wiederholen"):
            progress["correct_answers"] = 0
            progress["total_answers"] = 0
            progress["answers_detail"] = []
            progress["time_steps"] = []
            st.session_state["current_page"] = "Quiz"
            st.experimental_rerun()

def app():
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Quiz"
    if st.session_state["current_page"] == "Quiz":
        quiz_page()

app()