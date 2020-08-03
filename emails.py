#!/usr/bin/env python3

import sys
import os.path
import requests
import email.message
import mimetypes
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path = None):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if not attachment_path == None:
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _  = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split("/", 1)
        with open(attachment_path, "rb") as ap:
            message.add_attachment(ap.read(),
            maintype =  mime_type,
            subtype = mime_subtype,
            filename = attachment_filename)
            print("Email generated: {}\n".format(message))
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    print("Message sent\n")
    mail_server.quit()
