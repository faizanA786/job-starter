from google.cloud import firestore
from google.oauth2 import service_account
import json
import os
from datetime import datetime

firebase_service_account = json.loads(os.getenv("FIREBASE_SERVICE_ACCOUNT"))
credentials = service_account.Credentials.from_service_account_info(firebase_service_account)

db = firestore.Client(credentials=credentials)

pending = db.collection("pendingEmails")
subscribed = db.collection("subscribedEmails")
delete = db.collection("deleteEmails")
pending_docs = pending.stream()
subscribed_docs = list(subscribed.stream())
delete_docs = delete.stream()

# GET ALL SUBBED EMAILS
sub_emails = []
for doc in subscribed_docs:
    email = doc.to_dict().get("email")
    if email and email not in sub_emails:
        sub_emails.append(email)

# PROCESS REQUESTS TO REMOVE EMAILS
for doc in delete_docs:
    del_email = doc.to_dict().get("email")
    if del_email in sub_emails:

        get_doc = subscribed.where(filter=("email", "==", del_email)).stream()
        for sub_doc in get_doc:
            subscribed.document(sub_doc.id).delete()
    # print("removed " + del_email)
    delete.document(doc.id).delete()

# ADD/REMOVE DUPLICATE EMAILS
if len(subscribed_docs) < 100:
    for doc in pending_docs:
        fields = doc.to_dict()
        pen_email = fields.get("email")
        time_sent = fields.get("timestamp")

        if pen_email in sub_emails:
            # print("removed " + pen_email + ", already subscribed")
            pending.document(doc.id).delete()
        else:
            # print("added " + pen_email)
            subscribed.add({
                "email": pen_email,
                "time_sent": time_sent,
                "time_added": datetime.now()
                })
            pending.document(doc.id).delete()
else:
    print("Oversubscribed")