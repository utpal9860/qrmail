import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('foundationdayreal-firebase-adminsdk-4utqu-4e53a80def.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
count = 0
docs = db.collection('students').get()

for doc in docs:
    count += 1
    print(count)
    db.collection('students').document(doc.id).update({"status": "Absent"})
    # doc.update({
    # "status": "Absent"
    # })
    print(count)
