import smtplib
from email.message import EmailMessage

def send_email(subject,body):
    sender_email="sender@gmail.com"
    receiver_email="receiver@pw.live"
    password="sender_password"

    msg = EmailMessage()
    msg["subject"]=subject
    msg["from"]=sender_email
    msg["to"]=receiver_email
    msg.set_content(body)
    
    ## Attach log file
    with open('app.log','rb') as f:
        msg.add_attachment(f.read(),filename="app.log",
                           maintype='text', subtype='plain')
    
    with smtplib.SMTP("smtp.gmail.com","587") as server:
        server.starttls() # encrypt the connection
        server.login(sender_email,password)
        server.send_message(msg)
        
send_email("Backup Completed","Please find attached the critical error logs")
