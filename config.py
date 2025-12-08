import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
