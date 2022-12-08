import smtplib, ssl
import os


def send_email(raw_message):
    host = "smtp-mail.outlook.com"
    port = 587

    username = "neil_mercury@hotmail.com"
    password = os.getenv("PASSWORD")

    receiver = "neil_mercury@yahoo.es"
    context = ssl.create_default_context()

    message = f"""\
Subject: News

From: {username}
{raw_message}
"""

    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.login(username, password)
        server.sendmail(username, receiver, message)
