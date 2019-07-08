import smtplib
import os
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject']  = "Hello World this is the subject"
msg['From'] = ''
msg['To'] = 'dhairyajain2001@gmail.com'
msg.set_content("This is my body... how you doing bitch??")
EMAIL_ADDRESS  = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    smtp.send_message(msg)
