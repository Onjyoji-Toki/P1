import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

def process_mail():
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    login_address = 'egoshi2525@gmail.com'
    login_password = 'wjxxeraebruuehjf'
    server.login(login_address, login_password)

    message = MIMEMultipart()
    message['Subject'] = 'プロセス終了'
    message['From'] = 'egoshi2525@gmail.com'
    message['To'] = 'yuryo1207@outlook.jp,suzuki.junya.4r@kyoto-u.ac.jp,hori.yusuke.55s@st.kyoto-u.ac.jp'
    sender_address = 'egoshi2525@gmail.com'
    recipient_address = ['yuryo1207@outlook.jp', 'suzuki.junya.4r@kyoto-u.ac.jp', 'hori.yusuke.55s@st.kyoto-u.ac.jp']
    text = MIMEText('プロセスが終了しました。')
    message.attach(text)
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(login_address, login_password)
        server.sendmail(sender_address, recipient_address, message.as_string())

if __name__ == '__main__':
    process_mail()
