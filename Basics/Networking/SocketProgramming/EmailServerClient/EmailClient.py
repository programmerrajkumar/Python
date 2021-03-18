import smtplib
from email.mime.text import MIMEText

body="Hi Test mail"

msg=MIMEText(body)
msg["From"]=""
msg["To"]=""
msg["Subject"]=""
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("username","password")
server.send(msg)
print("Mail sent")
server.quit()