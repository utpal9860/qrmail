import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import pandas as pd

df = pd.read_excel('sciencefy.xlsx')
cols = list(df.columns)
length = df[cols[0]].count()
print(length)


email = 'indiraincub@gmail.com'
password = 'DevelopeR@111'
emails = df[cols[3]]
num = df[cols[2]]
send_to_email = 'rohanpawar328@gmail.com'
subject = 'Indira silver jubilee excellence Awards 2019 invitation(QR code)'
message = 'You are cordially invited to Indira silver jubilee excellence Awards 2019 on 19th January (6:00 PM on wards) at Indira National School. We are sending you a unique QR code. Please download it and do not share this QR code as only one entry per QR code is permitted'
file_location = 'C:\\Users\\DEUS-EX MACHINA\\Desktop\\foundation\\'


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
for _ in range(5):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['Subject'] = subject
    msg['To'] = df[cols[3]].iloc[_]
    print(_,str(num.iloc[_]))
    msg.attach(MIMEText(message, 'plain'))
    filepath = file_location + str(num.iloc[_]) + '.png'
    if os.path.isfile(filepath):

        filename = os.path.basename(file_location + 'qr.png')
        attachment = open(filepath, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)


        text = msg.as_string()

        if _ > 1 and _ % 50 == 0:
            server.quit()
            time.sleep(60)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)

        server.sendmail(email, send_to_email, text)
        print("sent")
server.quit()
