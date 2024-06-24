# scripts/email_notifier.py
import smtplib
from email.mime.text import MIMEText
from config import Config

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = Config.EMAIL_SENDER
    msg['To'] = ', '.join(Config.EMAIL_RECIPIENTS)

    with smtplib.SMTP(Config.EMAIL_SERVER, Config.EMAIL_PORT) as server:
        server.starttls()
        server.login(Config.EMAIL_USERNAME, Config.EMAIL_PASSWORD)
        server.sendmail(Config.EMAIL_SENDER, Config.EMAIL_RECIPIENTS, msg.as_string())
