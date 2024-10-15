from os import getenv
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from carregar_email import escolher_template_email
from carregar_texto import escolher_template_texto


def send_mail(estado):
    load_dotenv()
    SMTP_SERVER = getenv('SMTP_SERVER')
    SMTP_PORT = getenv('SMTP_PORT')
    EMAIL_SENDER = getenv('EMAIL_SENDER')
    EMAIL_PASSWORD = getenv('EMAIL_PASSWORD')
    EMAIL_RECEIVER = getenv('EMAIL_RECEIVER')

    
    ASSUNTO = 'Status do Backup'

    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = ASSUNTO

    html_content = escolher_template_email(estado)
    msg.attach(MIMEText(html_content, 'html'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()  
            server.starttls()  
            server.ehlo() 
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
            print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')
