# coding = utf-8
# 2018.04.09

import smtplib
from email.mime.text import MIMEText
import base64


def send_email(subject='邮件主题', content='邮件正文', rec=list()):
    server = 'smtp.exmail.qq.com'
    port = 465
    username = 'fengziqi@inspiry.cn'
    password = base64.b64decode(b'RmVuZzEyMw==\n')
    msg = MIMEText(content, 'plain', 'utf-8')

    msg['Subject'] = subject
    msg['From'] = 'fengziqi@inspiry.cn'
    msg['To'] = 'fengziqi@inspiry.cn'

    try:
        s = smtplib.SMTP_SSL(server, port=port)
        s.login(username, password.decode())
        s.sendmail(msg['From'], rec, msg.as_string())
    except Exception as e:
        print(e)
    else:
        s.close()


if __name__ == "__main__":
    send_email()
