import json
import smtplib
import xlsxwriter
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

def send_mail_file(file_path, to = None):
    global params
    smtpObj = None
    try:        
        if to is None : to  = params["mail"]["to"]        

        msg = MIMEMultipart()
        msg['From'] = params["mail"]["from"]
        msg['To'] = to
        msg['Subject'] = params["mail"]["subject"]

        msg.attach(MIMEText(body_text, 'plain'))

        with open(file_path, 'rb') as f:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(encodebytes(f.read()).decode())
            part.add_header('Content-Transfer-Encoding', 'base64')
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % file_path)
            msg.attach(part)   


        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(params["mail"]["login"], params["mail"]["password"])
        smtpObj.sendmail(params["mail"]["from"], to, msg.as_string())

    finally:
        if smtpObj is not None:
                smtpObj.quit()


def write_smarts_to_xlsm(dic1, dic2):
    workbook = xlsxwriter.Workbook('smarts_title_price.xlsm')
    ws_top = workbook.add_worksheet("top") 
    ws_filtered = workbook.add_worksheet("filtered") 

    # dic1 :  [(title, price),() ....]

    total,row, col = 0,0,0
    for title, price in dic1:
        ws_top.write(row,col, str(title))
        ws_top.write(row,col+1, price)
        row +=1
        total +=1 


    row = 0
    for title, price in dic2:
        ws_filtered.write(row,col, str(title))
        ws_filtered.write(row,col+1, price)
        row +=1
        total +=1

        
    workbook.close()

    return total
