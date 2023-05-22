import smtplib, ssl
from email.message import EmailMessage
import datetime, time

import passwords

password = passwords.auth['password']



sender = 'dolati.hamidreza78@gmail.com'
receiver = 'fgh5991@gmail.com'

while True :
    time.sleep(60)
    if datetime.datetime.now().strftime('%Y-%m-%d %H:%M') == '2022-10-03 18:24':
        subject = "Test email"
        body = """
this is a test email to checkout how my automation works!!!
        """

        em = EmailMessage()
        em['From'] = sender
        em['To'] = receiver
        em['subject'] = subject
        em.set_content(body)


        context = ssl.create_default_context()
        port = 465
        with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, em.as_string())
        break
    