import streamlit as st
import pandas as pd

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