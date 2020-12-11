# Run the below commands in the terminal before executing the program
# export EMAIL_USER="<email address>"
# export EMAIL_PASS="<email password>"

import smtplib, ssl
from email.message import EmailMessage
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['From'] = "iotsatish25@gmail.com"
msg['To'] = "tcs.satish@gmail.com,theiotusersclub@gmail.com"
msg['Subject'] = 'IoT Check Alert'
msg.set_content('This is a plain text email')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

