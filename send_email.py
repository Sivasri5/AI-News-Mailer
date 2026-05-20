import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "sivasrir.22cse@kongu.edu"
    password = os.getenv("MAIL_PASSWORD")

    receiver = "sivasrir.22cse@kongu.edu"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)

