import os
import shutil
from datetime import datetime
import logging
import smtplib
from email.mime.text import MIMEText

def send_email(subject,body):
    sender_email="sender@gmail.com"
    receiver_email="receiver@pw.live"
    password="sender_password"

    msg = MIMEText(body)
    msg["subject"]=subject
    msg["from"]=sender_email
    msg["to"]=receiver_email
    
    with smtplib.SMTP("smtp.gmail.com","587") as server:
        server.starttls() # encrypt the connection
        server.login(sender_email,password)
        server.send_message(msg)

logging.basicConfig(
    filename='backuplogs.log',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
try:
    #folder to take a backup
    source_folder = "files"
    # Where to store backups
    backup_folder = "backups"
    os.makedirs(backup_folder,exist_ok=True)
    #Generate timestamps
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    #Construct Backupfile name with timestamp
    backup_filename=f"{backup_folder}/backup_{timestamp}"
    #Create zip archive
    shutil.make_archive(backup_filename,'zip',source_folder)
    logging.info(f"Backup Created {backup_filename}.zip")
    send_email("Backup Completed",f"Backup Created {backup_filename}.zip")
except Exception as e:
    logging.error(f"Backup failed: {e}")
    

