import pymongo
import os
from dotenv import load_dotenv
from nanoid import generate

load_dotenv()  # take environment variables from .env.

db_url = os.environ.get("DATABASE_URL")
print(db_url)
myclient = pymongo.MongoClient(db_url)
mydb = myclient["webssh"]

mycol = mydb["ssh_servers"]


mydict = { "name": "John", "address": "Highway 37", 'nid': generate(size=11) }

x = mycol.insert_one(mydict)
print(x.inserted_id)
print(mydict)