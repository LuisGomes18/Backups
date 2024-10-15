import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


load_dotenv()
smtp_server = 'Colocar o server pedendo do email usado'
smtp_port = 'porta do smtp'
email_sender = 'email que sera enviado'
email_password = 'password da conta'


email_receiver = 'email que ira receber o email'
subject = 'Assunto do E-mail'
body = 'Este é o corpo do e-mail.'


msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))


try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(email_sender, email_password)  
        server.send_message(msg)  
    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')
