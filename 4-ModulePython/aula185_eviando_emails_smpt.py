# Enviando E-mails SMPT com Python
import os
import pathlib
from string import Template
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

# Caminho arquivo HMTL
CAMIMNHO_HTML = pathlib.Path(__file__).parent / 'aula185.html'

# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Configurações SMPT
smpt_server = 'smpt.gmail.com'
smpt_port = 587
smpt_username = os.getenv('FROM_EMAIL', '')
smpt_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
with open(CAMIMNHO_HTML, 'r') as file:
    texto_arquivo = file.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='João')

# print(texto_email)

# Transformar nossa menssagem em MIMEmultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)


# Envia o E-mail
with smtplib.SMTP(smpt_server, smpt_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smpt_username, smpt_password)
    server.send_message(mime_multipart)
    print('E-MAIL ENVIADO COM SUCESSO!')
    print()

