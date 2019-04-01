# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ----------1.跟发件相关的参数------
smtpserver = "smtp.163.com"  # 发件服务器
# smtpserver = "smtp.qq.com"
port = 0  # 端口
# port = 465
sender = "yoyo@163.com"  # 账号
psw = "**************"  # 密码
# receiver = "283340479@qq.com"  # 接收人
receiver = ["xxxx@qq.com", "yoyo@qq.com"] # 多个收件人 list 对象
# ----------2.编辑邮件的内容------
# subject = "这个是主题 163"
# body = '<p>这个是发送的 163 邮件</p>'  # 定义邮件正文为 html 格式
# msg = MIMEText(body, "html", "utf-8")
# msg['from'] = sender
# msg['to'] = "283340479@qq.com"
# msg['subject'] = subject
# 读文件
file_path = "result.html"
with open(file_path, "rb") as fp:
    mail_body = fp.read()
msg = MIMEMultipart()
msg["from"] = sender # 发件人
# msg["to"] = receiver # 收件人
msg["to"] = ";".join(receiver) # 多个收件人 list 转 str
msg["subject"] = "这个我的主题" # 主题
# 正文
body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)
# 附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)
# ----------3.发送邮件------
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)  # 连服务器
# # smtp = smtplib.SMTP_SSL(smtpserver, port)
# smtp.login(sender, psw)  # 登录
# smtp.sendmail(sender, receiver, msg.as_string())  # 发送
# smtp.quit()  # 关闭
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())  # 发送
smtp.quit()  # 关闭