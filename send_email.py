import smtplib
import ssl
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    email = os.getenv("SMTP_EMAIL")
    password = os.getenv("SMTP_PASSWORD")
    receiver = os.getenv("SMTP_RECEIVER")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, receiver, message)
