import firebase_admin
from firebase_admin import credentials, firestore
import json
import resend
import os
import time

cred = credentials.Certificate("job_starter/firebase-service-account.json")  
firebase_admin.initialize_app(cred)
db = firestore.client()

subscribed = db.collection("subscribedEmails")
subscribed_docs = list(subscribed.stream())

# GET ALL SUBBED EMAILS
sub_emails = []
for doc in subscribed_docs:
    email = doc.to_dict().get("email")
    if email and email not in sub_emails:
        sub_emails.append(email)

# GET JOB STATS
jsons = ["job_starter/prefetch/logistics_data.json", "job_starter/prefetch/retail_data.json", "job_starter/prefetch/hospitality_data.json"]
lengths = []

def get_length(open_url): # in this context, length just means the num of jobs posted today/yesterday
    length = 0
    with open(open_url, "r", encoding="utf-8") as f: 
        industry = json.load(f)
        for job in industry:
            if job["date"] == "Today" or job["date"] == "Yesterday":
                length += 1
    return length

for i in range(len(jsons)):
    lengths.append(get_length(jsons[i]))

# SEND DAILY MAIL
resend.api_key = os.getenv("RESEND_API_KEY")
for email in sub_emails:
    try:
        resend.Emails.send({
            "from": "job-starter@jobstarter.uk",
            "to": [email],
            "subject": "Jobs Posted Recently",
            "html": f"""
                <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background-color: #f4f4f4;
                            margin: 0;
                            padding: 0;
                        }}
                        .container {{
                            width: 100%;
                            max-width: 600px;
                            margin: 0 auto;
                            background-color: #ffffff;
                            padding: 20px;
                            border-radius: 8px;
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                        }}
                        h1 {{
                            color: #333333;
                            text-align: center;
                        }}
                        h2 {{
                            color: #555555;
                            font-size: 18px;
                            margin: 10px 0;
                        }}
                        a {{
                            display: block;
                            width: 100%;
                            text-align: center;
                            padding: 10px;
                            background-color: #007bff;
                            color: white;
                            text-decoration: none;
                            border-radius: 4px;
                            margin-top: 20px;
                        }}
                        a:hover {{
                            background-color: #0056b3;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Recent Job Updates</h1>
                        <h2>There are {lengths[0]} new job in logistics</h2>
                        <h2>There are {lengths[1]} new jobs in retail</h2>
                        <h2>There are {lengths[2]} new jobs in hospitality</h2>
                        <a href="http://jobstarter.uk/" target="_blank"><h2>Visit Job Starter</h2></a>
                    </div>
                </body>
                </html>
            """
        })
        print("mail sent to " + email)
        time.sleep(1)

    except Exception as error:
        print("failed to send mail to " + email + ": " + error)
