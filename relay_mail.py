import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

def relay_mail():
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    login_address = 'egoshi2525@gmail.com'
    login_password = 'wjxxeraebruuehjf'
    server.login(login_address, login_password)

    message = MIMEMultipart()
    message['Subject'] = 'リレー異常検知'
    message['From'] = 'egoshi2525@gmail.com'
    message['To'] = 'yuryo1207@outlook.jp'
    sender_address = 'egoshi2525@gmail.com'
    recipient_address = 'yuryo1207@outlook.jp'
    text = MIMEText('リレーとの接続に失敗しました')
    message.attach(text)
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(login_address, login_password)
        server.sendmail(sender_address, recipient_address, message.as_string())