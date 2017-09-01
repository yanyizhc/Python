#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def email(areceiver, Subject, body, stlist):
    sever_host = "smtp.163.com"     # 邮箱服务器
    sender = '18874832147@163.com'  # 邮箱账号
    sender_pwd = 'YanYi11aillp'     # 邮箱密码
    msg = MIMEMultipart()
    b = 0
    if len(stlist) != 0:
        for a in range(len(stlist)):
            stlistxl = stlist[b]
            file_name = stlistxl.rsplit('/', 1)[1]
            att = MIMEApplication(open(stlistxl, 'rb').read())
            att.add_header('Content-Disposition', 'attachment', filename=file_name)
            msg.attach(att)
            b += 1
    else:
        pass
    msg['Subject'] = Subject  # 主题
    msg['To'] = formataddr(["cphelp", areceiver])
    msg['From'] = formataddr(["zhc", sender])
    text1 = MIMEText(body, 'plain', 'utf-8')
    msg.attach(text1)
    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(sever_host)
        smtpObj.login(sender, sender_pwd)
        smtpObj.sendmail(sender, areceiver, msg.as_string())
        print u"邮件发送成功"
        smtpObj.quit()
    except smtplib.SMTPException:
        print u"Error:无法发送邮件"

areceiver = '411720578@qq.com'
Subject = '送邮测试'
body = '''发送邮件测试正文'''
# 'C:/Users/Administrator/Desktop/email_text.txt', 'C:/Users/Administrator/Desktop/email_text2.xls'
stlist = []
email(areceiver, Subject, body, stlist)