# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import math

# pH-Rechner
st.title("pH-Rechner")
c_h3o = st.number_input("Konzentration [H₃O⁺] in mol/L")
if c_h3o > 0:
    ph = -math.log10(c_h3o)
    st.write(f"pH-Wert: {ph:.2f}")
else:
    st.write("Bitte geben Sie eine gültige Konzentration > 0 ein.")