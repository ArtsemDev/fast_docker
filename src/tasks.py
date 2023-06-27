import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.celery import celery, SETTINGS


@celery.task
def ping(to: str, subject: str, payload: str):
    msg = MIMEMultipart()
    msg['From'] = SETTINGS.SMTP_USER
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(payload))

    server = smtplib.SMTP(SETTINGS.SMTP_HOST, SETTINGS.SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(SETTINGS.SMTP_USER, SETTINGS.SMTP_PASSWORD.get_secret_value())
    server.sendmail(
        SETTINGS.SMTP_USER,
        to,
        msg.as_string()
    )
    server.quit()
