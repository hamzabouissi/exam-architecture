
import os
from pymongo import MongoClient


def create_subscriber(email:str) -> list[str]:
    # Initialize DynamoDB table
    table_name = os.getenv("MONGO_TABLE_NAME")
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client["exams"]
    collection = db[table_name]
    subscribers = collection.insert_one({"email":email})
    return subscribers


def handler(event,context):
    email = event['traits']['email']
    create_subscriber(email)