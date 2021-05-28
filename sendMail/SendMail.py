import smtplib
import ssl

DADOS_EMAIL = {
    "port": 587,
    "smtp_server": "smtp.gmail.com",
    "sender_email": "email",
    "receiver_email": "email",
    "password": 'SENHA_APP'
}

# Função para enviar emails


def sendEmail(dadosEmail, nomeBanco, nomeUsuario):

    message = nomeUsuario+', favor confirmar se o banco de dados: "' + \
        nomeBanco + '", devera permanecer com a classificacao: "HIGH"'

    context = ssl.create_default_context()
    with smtplib.SMTP(dadosEmail['smtp_server'], dadosEmail['port']) as server:
        server.starttls(context=context)
        server.login(dadosEmail['sender_email'], dadosEmail['password'])
        server.sendmail(
            dadosEmail['sender_email'], dadosEmail['receiver_email'], message)
    print(message)


sendEmail(DADOS_EMAIL, "Banco Producao", "Sr. Jorge")
