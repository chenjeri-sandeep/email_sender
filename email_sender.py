from os import path
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())


email = EmailMessage()
email["from"] = "Sandy"
email["to"] = "John@gmail.com"
email["subject"] = "Sub:Sick leave"
# email.set_content("i'm python master!!")
email.set_content(html.substitute({"name": "John"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("dumtest865@gmail.com", "$A&Y@865")
    smtp.send_message(email)
    print("all good boss!!")
