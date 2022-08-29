import smtplib
import ssl
from email.message import EmailMessage

email_sender = "vald3nir@gmail.com"
email_password = "yzmqcfqgnfwwdsun"

# https://temp-mail.org/pt
email_receiver = "sifan96910@otodir.com"

subject = "Teste"
body = """
Exemplo de um texto de teste
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

if __name__ == '__main__':
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
