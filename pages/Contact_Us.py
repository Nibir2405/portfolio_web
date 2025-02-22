import streamlit as st
from send_email import send_mail

st.header("Contact Me")

with st.form(key="contact form"):

    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message")
    message = f"""\
    Subject: New mail about portfolio Webapp

    From: {user_email}
    {raw_message}"""

    submit = st.form_submit_button()
    if submit:
        send_mail(message)
        st.info("Your message was sent successfully")