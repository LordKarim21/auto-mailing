import smtplib
from email.mime.text import MIMEText

SERVER = ''
PORT = 465
LOGIN = ''
PASSWORD = ''
FROM_EMAIL = ''
TEXT_TYPE = 'plain'


def send_email(to, subject, message):
    msg = MIMEText(message, TEXT_TYPE, 'utf-8')
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to

    smtp = smtplib.SMTP(SERVER, 587)
    smtp.starttls()
    smtp.login(LOGIN, PASSWORD)
    smtp.send_message(msg)
    smtp.quit()


if __name__ == '__main__':
    send_email('', 'Тема письма', 'Тело письма')
