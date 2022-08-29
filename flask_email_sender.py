"""
Setup:
pip install Flask, Flask-Mail
"""

from flask_mail import Mail, Message

from flask import Flask

email_sender = "vald3nir@gmail.com"
email_password = "yzmqcfqgnfwwdsun"

# https://temp-mail.org/pt
email_receiver = "sifan96910@otodir.com"

subject = "Teste"
body = """
Exemplo de um texto de teste
"""

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email_sender,
    "MAIL_PASSWORD": email_password
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    with app.app_context():
        msg = Message(
            subject=subject,
            sender=email_sender,
            recipients=[email_receiver],
            body=body
        )
        mail.send(msg)
