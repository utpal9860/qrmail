import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd


# df = pd.read_excel('comp_mech_icem.xlsx')
# cols = list(df.columns)
# length = df[cols[0]].count()
# print(length)
cred = credentials.Certificate('indirajubilee2019-firebase-adminsdk-g6tiv-b283172769.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
# for _ in range(length):
#     print(_)
doc_ref = db.collection('students').document('9359068751').update({

    "status":"Absent"

})
