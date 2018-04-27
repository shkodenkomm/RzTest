import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pymongo import MongoClient

params = {}

def get_params():
    with open("config.json", encoding="utf8", mode="r") as f :
        return json.load(f)

def send_mail(body_text):
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
        smtpObj.sendmail(params["mail"]["from"], params["mail"]["to"], msg.as_string())

    finally:
        if smtpObj is not None:
                smtpObj.quit()

def save_to_db(obj):
    global params
    client = MongoClient(params["db"]["host"], params["db"]["port"])
    db = client['rz']
    cl = db.get_collection("test_results")

    id = cl.insert_one(obj)

    return id
