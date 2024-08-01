import base64
from email.mime.text import MIMEText
from email.message import EmailMessage
import smtplib
from requests import HTTPError
import requests
from pymongo import MongoClient
import os


API_KEY = os.environ['MAILGUN_API_KEY']

def get_subscribers() -> list[str]:
    # Initialize DynamoDB table
    table_name = os.getenv("MONGO_TABLE_NAME")
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client["exams"]
    collection = db[table_name]
    subscribers = collection.find()
    return list(e['email'] for e in subscribers )


def main(event, context):
    body = event.decode()
    subs = get_subscribers()
    requests.post(
        "https://api.mailgun.net/v3/sandboxbc48ab1481934d378c0a7bcccee35cbb.mailgun.org/messages",
        auth=("api", API_KEY),
        data={
            "from": "Excited User <no-reply@enkinineveh.space>",
            "to": subs,
            "subject": "Hello",
            "text": body,
        },
    )
