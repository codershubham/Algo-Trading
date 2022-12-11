import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def send_mail(messege):
    if len(messege) <= 26:
        return

    msg = EmailMessage()
    msg['Subject'] = 'Stock Alert!! AlgoTrader'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    msg.set_content(messege)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
