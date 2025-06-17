import os
import smtplib


def send_email(user_message):
    host = "smtp.gmail.com"
    port = 587
    username = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    receiver = os.getenv('EMAIL')

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        user_message['From'] = username
        user_message["To"] = receiver
        server.send_message(user_message)
