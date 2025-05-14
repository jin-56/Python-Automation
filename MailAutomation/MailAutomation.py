import smtplib
from email.mime.text import MIMEText


smtp_server = "smtp.gmail.com"
smtp_port = 465
username ='your_mail_99@gmail.com'
password = '123456789'

recepients=["recipient_person@gmail.com"]

#What you type will be the mail description.
subject = "Testing mail automation"
body = "Hello There"      
message=MIMEText(body,"plain")
message['Subject']=subject
message["To"]=",".join(recepients)

with smtplib.SMTP(smtp_server,smtp_port) as server:
    server.starttls()
    server.login(username,password)
    for recipient in recepients:
        server.sendmail(username,recipient,message.as_string())
        print(f"Mail sent to {recipient}")
        
print("Done")
        
        