import pyqrcode
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

df = pd.read_excel('extra.xlsx')
cols = list(df.columns)
length = df[cols[0]].count()
print(length)
cred = credentials.Certificate('indirajubilee2019-firebase-adminsdk-g6tiv-b283172769.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
for _ in range(length):
    print(_)
    doc_ref = db.collection('students').document(str(df[cols[2]].iloc[_])).set({
        "name" : df[cols[1]].iloc[_],
        "number" : str(df[cols[2]].iloc[_]),
        "gmail" : df[cols[3]].iloc[_],
        "status":"Absent"

    })
    nos = list(str(df[cols[2]].iloc[_]))
    string = ""
    for i in range (len(nos)):
        string += chr(97 + int(nos[i]) + i)
    print(string,df[cols[2]].iloc[_])
    big_code = pyqrcode.create(string, error='L', version=1, mode='binary')
    big_code.png(str(df[cols[2]].iloc[_])+'.png', scale=5, module_color=[0, 0, 0], background=[0xff, 0xff, 0xff])
    # big_code.show()
# print(_)


#qrcode
# big_code = pyqrcode.create('7030127734', error='L', version=1, mode='binary')
# big_code.png('7030127734.png', scale=5, module_color=[0, 0, 0], background=[0xff, 0xff, 0xcc])
# big_code.show()
