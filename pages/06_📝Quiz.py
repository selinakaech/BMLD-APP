# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import random
import pandas as pd
import base64

# Funktion, um den Hintergrund per Bild-URL zu setzen
def set_background_from_url(image_url): 
    st.markdown(
        f"""
<style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.4)), 
                              url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: top; /* Verschiebt das Bild nach oben */
        }}
</style>
        """,
        unsafe_allow_html=True
    )

# Deine Bild-URL
image_url = "https://img.freepik.com/vektoren-kostenlos/hintergrund-mit-fragezeichen_78370-2896.jpg?semt=ais_hybrid&w=740"

# Hintergrund setzen
set_background_from_url(image_url)

# Liste von 15 statischen Fragen und Antworten
questions = [
    {"question": "Was ist die chemische Formel von Wasser?", "answer": "H2O"},
    {"question": "Welches Element hat das Symbol H?", "answer": "Wasserstoff"},
    {"question": "Welches Element hat das Symbol O?", "answer": "Sauerstoff"},
    {"question": "Wie viele Protonen hat ein Wasserstoffatom?", "answer": "1"},
    {"question": "Was ist die chemische Formel von Kohlendioxid?", "answer": "CO2"},
    {"question": "Was ist der pH-Wert von reinem Wasser?", "answer": "7"},
    {"question": "Welches Element hat das Symbol Na?", "answer": "Natrium"},
    {"question": "Was ist der Aggregatzustand von Eis bei Raumtemperatur?", "answer": "fest"},
    {"question": "Was ist der Aggregatzustand von Sauerstoff bei Raumtemperatur?", "answer": "gasförmig"},
    {"question": "Wie lautet die Ordnungszahl von Sauerstoff?", "answer": "8"},
    {"question": "Was ist die chemische Formel von Kochsalz?", "answer": "NaCl"},
    {"question": "Wie nennt man das Element mit der Ordnungszahl 1?", "answer": "Wasserstoff"},
    {"question": "Was ist der pKs-Wert von Salzsäure?", "answer": "-6"},
    {"question": "Welche Farbe hat Schwefel in Reinform?", "answer": "gelb"},
    {"question": "Welches Element hat das Symbol He?", "answer": "Helium"}
]

# Definiere den Lernfortschritt
progress = {
    "correct_answers": 0,
    "total_answers": 0,
    "answers_detail": [],
    "time_steps": [],
}

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

    st.success("Antworten gespeichert")
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
        st.rerun()

# Feedback basierend auf der Anzahl richtiger Antworten
if progress["correct_answers"] == progress["total_answers"]:
    st.success("🎉 Perfekt! Du hast alle Fragen richtig beantwortet. Großartige Arbeit!")
elif progress["correct_answers"] >= progress["total_answers"] * 0.8:
    st.info("👍 Sehr gut! Du hast die meisten Fragen richtig beantwortet. Weiter so!")
elif progress["correct_answers"] >= progress["total_answers"] * 0.5:
    st.warning("🙂 Nicht schlecht! Du hast mehr als die Hälfte richtig. Übung macht den Meister!")
else:
    st.error("😅 Das war wohl nicht dein Tag. Versuch es nochmal, du schaffst das!")



# Einfügen des Logos in die Sidebar
# Funktion, um ein Bild in Base64 zu konvertieren
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Lokaler Pfad zum Bild
sidebar_logo_path = "docs/Images/Logo Labmate.png"  # Passe den Pfad an, falls nötig

# Lokaler Pfad zum Bild
sidebar_logo_path = "docs/Images/Logo Labmate.png"  # Passe den Pfad an, falls nötig

# Fehlerbehandlung für das Laden des Bildes
try:
    logo_base64 = get_base64_image(sidebar_logo_path)
    # Logo in der Sidebar einfügen
    st.sidebar.markdown(
        f"""
        <div style="text-align: center; padding: 10px 0;">
            <img src="data:image/png;base64,{logo_base64}" alt="Logo" style="width: 150px;">
        </div>
        """,
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.sidebar.error("Das Logo wurde nicht gefunden. Überprüfe den Pfad.")