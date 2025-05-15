import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Quiz-Daten vorhanden. Bitte machen Sie zuerst ein Quiz.')
    st.stop()

# Sort dataframe by timestamp, falls vorhanden
if 'timestamp' in data_df.columns:
    data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)

# Lernfortschritt berechnen und anzeigen
if 'correct_answers' in data_df.columns and 'total_answers' in data_df.columns:
    gesamt_richtig = data_df['correct_answers'].sum()
    gesamt_gesamt = data_df['total_answers'].sum()
    fortschritt = (gesamt_richtig / gesamt_gesamt) * 100 if gesamt_gesamt > 0 else 0
    st.metric("Gesamter Lernfortschritt", f"{fortschritt:.1f} %")

    # Graph 1: Fortschritt pro Quiz (Balkendiagramm)
    st.subheader("Fortschritt pro Quiz")
    fig1, ax1 = plt.subplots()
    fortschritt_pro_quiz = (data_df['correct_answers'] / data_df['total_answers']) * 100
    ax1.bar(data_df.index, fortschritt_pro_quiz)
    ax1.set_xlabel("Quiz-Versuch")
    ax1.set_ylabel("Richtige Antworten (%)")
    ax1.set_title("Richtige Antworten pro Quiz")
    st.pyplot(fig1)

    # Graph 2: Kumulativer Fortschritt über die Zeit (Liniendiagramm)
    st.subheader("Kumulativer Lernfortschritt")
    fig2, ax2 = plt.subplots()
    kumulativ_richtig = data_df['correct_answers'].cumsum()
    kumulativ_gesamt = data_df['total_answers'].cumsum()
    kumulativ_fortschritt = (kumulativ_richtig / kumulativ_gesamt) * 100
    ax2.plot(kumulativ_fortschritt, marker='o')
    ax2.set_xlabel("Quiz-Versuch")
    ax2.set_ylabel("Kumulierter Fortschritt (%)")
    ax2.set_title("Kumulativer Lernfortschritt")
    ax2.set_ylim(0, 100)
    st.pyplot(fig2)