import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sender(recipients): 

    body = 'Tugas besar saya'
    msg = MIMEMultipart()

    msg['Subject'] = 'Tugas Besar'
    msg['From'] = 'hammam@example.com'
    msg['To'] = ('john@example.com, mike@example.com').join(recipients.split(','))

    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('hamam@example.com', 'hhhhhh')
    server.send_message(msg)
    server.quit()