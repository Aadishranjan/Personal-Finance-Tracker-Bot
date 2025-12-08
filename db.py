from pymongo import MongoClient
from config import MONGO_URL, DB_NAME
from datetime import datetime

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

users = db.users
transactions = db.transactions   # one collection for expenses + savings


# Save user
def add_user(user_id, name, username):
    if not users.find_one({"user_id": user_id}):
        users.insert_one({
            "user_id": user_id,
            "first_name": name,
            "username": username
        })


# Save expense
def expense(user_id, amount, category):
    transactions.insert_one({
        "user_id": user_id,
        "type": "expense",
        "amount": amount,
        "category": category,
        "date": datetime.now()
    })


# Save saving
def saving(user_id, amount):
    transactions.insert_one({
        "user_id": user_id,
        "type": "saving",
        "amount": amount,
        "date": datetime.now()
    })


# Fetch all users for reminder
def get_all_users():
    return users.find()
