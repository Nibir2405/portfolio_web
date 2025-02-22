from numpy import less
import streamlit as st

st.header("Contact Me")

with st.form(key="contact from"):

    user_email = st.text_input("Your Email Address")
    message = st.text_area("Your Message")
    submit = st.form_submit_button()
    if submit:
        print("submitted")