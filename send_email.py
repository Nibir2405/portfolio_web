import smtplib
import ssl

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    email = "nibirislam56@gmail.com"

    password = "xxabkwlcvtydocoj"

    receiver = "navidulislam2002@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email,password)
        server.sendmail(email, receiver, message)
