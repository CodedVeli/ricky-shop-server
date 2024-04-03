import smtplib
from email.mime.text import MIMEText
from flask import jsonify

# sender_email = "ericgithaiga007@gmail.com"
# sender_password = "gjwn hajc tols wlui "
# recipient_email = "erickgithaiga28@gmail.com"
# subject = "Hello from Ricky's Shop"
# with open('signup.html', 'r')  as body:
#     body = body.read()

# html_message = MIMEText(body, 'html')
# html_message['Subject'] = subject
# html_message['From'] = sender_email
# html_message['To'] = recipient_email
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
#    server.login(sender_email, sender_password)
#    server.sendmail(sender_email, recipient_email, html_message.as_string())


def send_signup_email(sender_email, sender_password, recipient_email, subject, body):
    html_message = MIMEText(body, 'html')
    html_message['Subject'] = subject
    html_message['From'] = sender_email
    html_message['To'] = recipient_email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, html_message.as_string())
    except smtplib.SMTPRecipientsRefused:
        return jsonify({'message': 'Please enter a valid email'}), 400
# send_signup_email( sender_email, sender_password, recipient_email, subject, body)