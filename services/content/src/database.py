import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
DATABASE_URL = f"{os.environ['DATABASE_URL']}?retryWrites=true&w=majority"

client = MongoClient(DATABASE_URL)
db = client.newoola_places
