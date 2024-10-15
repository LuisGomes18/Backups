from os import getcwd, path, getenv
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.json_handler import carregar_configuracao


def carregar_template_inicio():
    diretorio_projeto = getcwd()
    diretorio_templates = path.join(diretorio_projeto, 'templates')

    try:
        with open(path.join(diretorio_templates, 'inicio_backup.html'), 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError('Arquivo de configura o n o encontrado!')
    except Exception as error:
        raise Exception(f'Erro inesperado ao carregar o arquivo de configura o: {error}')


def carregar_template_finalizar():
    diretorio_projeto = getcwd()
    diretorio_templates = path.join(diretorio_projeto, 'templates')

    try:
        with open(path.join(diretorio_templates, 'finalizar_backup.html'), 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError('Arquivo de configuração não encontrado!')
    except Exception as error:
        raise Exception(f'Erro inesperado ao carregar o arquivo de configuração: {error}')


def escolher_html(estado):
    if not estado or estado.lower() not in ["comecar", "finalizar"]:
        raise ValueError(f'Estado inválido: {estado}')

    if estado.lower() == "comecar":
        return carregar_template_inicio()
    else:
        return carregar_template_finalizar()


def mandar_email(estado):
    load_dotenv()

    SMTP_SERVER = getenv('SMTP_SERVER')
    SMTP_PORT = getenv('SMTP_PORT')
    EMAIL_SENDER = getenv('EMAIL_SENDER')
    EMAIL_PASSWORD = getenv('EMAIL_PASSWORD')

    configuracao = carregar_configuracao()
    EMAIL_RECEIVER = configuracao["email_destinatario"]
    print(EMAIL_RECEIVER)

    ASSUNTO = "Status do Backup"

    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = ASSUNTO

    html_content = escolher_html(estado)
    msg.attach(MIMEText(html_content, 'html'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

        print('E-mail enviado com sucesso!')
    except Exception as error:
        raise Exception(f'Erro inesperado ao enviar o e-mail: {error}')
