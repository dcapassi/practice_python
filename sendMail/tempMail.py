import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DADOS_EMAIL = {
    "port": 587,
    "smtp_server": "smtp.gmail.com",
    "sender_email": "thiagomandouemail@gmail.com",
    "receiver_email": "diego.capassi.moreira@gmail.com",
    "password": 'H0m3w0rk@2020'
}

# Função para enviar emails


def sendEmail(dadosEmail, nomeBanco, nomeUsuario):
    msg = MIMEMultipart()
    msg['From'] = dadosEmail['sender_email']
    msg['To'] = dadosEmail['receiver_email']
    msg['Subject'] = 'Verificacao Db'

    body = nomeUsuario+', favor confirmar se o banco de dados: "' + \
        nomeBanco + '", devera permanecer com a classificacao: "HIGH"'
    message = MIMEText(body, 'plain')
    msg.attach(message)

    context = ssl.create_default_context()
    with smtplib.SMTP(dadosEmail['smtp_server'], dadosEmail['port']) as server:
        server.starttls(context=context)
        server.login(dadosEmail['sender_email'], dadosEmail['password'])
        server.sendmail(
            dadosEmail['sender_email'], dadosEmail['receiver_email'], msg.as_string())
    print(msg.as_string())


sendEmail(DADOS_EMAIL, "Usuarios", "Sr. Jorge")
