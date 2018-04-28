import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pymongo import MongoClient

params = {}

def get_params():
    with open("config.json", encoding="utf8", mode="r") as f :
        return json.load(f)

def send_mail(body_text, to = None):
    global params
    smtpObj = None
    try:
        msg = MIMEMultipart()
        msg['From'] = params["mail"]["from"]
        msg['To'] = params["mail"]["to"]
        msg['Subject'] = params["mail"]["subject"]

        msg.attach(MIMEText(body_text, 'plain'))

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(params["mail"]["login"], params["mail"]["password"])
        if to is None : to  = params["mail"]["to"]
        smtpObj.sendmail(params["mail"]["from"], to, msg.as_string())

    finally:
        if smtpObj is not None:
                smtpObj.quit()

def send_mail_to_list(body_text):
    with open("mail_list.json", encoding="utf8", mode="r") as f :
        mail_list = json.load(f)

    for m in mail_list:
        sendmail(body_text, m)

def save_to_db(obj):
    global params
    client = MongoClient("localhost", 27017)
    db = client['rz']
    cl = db.get_collection("test_results")

    id = cl.insert_one(obj)

    return id
