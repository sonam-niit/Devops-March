import smtplib
from email.mime.text import MIMEText

def send_email(subject,body):
    sender_email="your_email@gmail.com"
    receiver_email="receiver_email@pw.live"
    password="write your password"

    #go to https://myaccount.google.com
    # select>security> enable 2 step-verification
    # Search bar > app password
    # create new password and use it
    msg = MIMEText(body)
    msg["subject"]=subject
    msg["from"]=sender_email
    msg["to"]=receiver_email
    
    with smtplib.SMTP("smtp.gmail.com","587") as server:
        server.starttls() # encrypt the connection
        server.login(sender_email,password)
        server.send_message(msg)
        
send_email("Backup Completed","Backup Created Successfully")
