import pymongo
import os
from dotenv import load_dotenv

def connectdb():
    load_dotenv()
    db_url = os.environ.get("DATABASE_URL")
    print(db_url)
    return pymongo.MongoClient(db_url)

class MongoManager:
     __db = "webssh"
     __instance = None
     @staticmethod 
     def getInstance():
         if MongoManager.__instance == None:
             MongoManager()
         return MongoManager.__instance

     @classmethod
     def db(cls):
        return cls.getInstance()[cls.__db]

     @classmethod
     def col(cls, name: str):
        return cls.db()[name]

     def __init__(self):
        if MongoManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MongoManager.__instance = connectdb()

def get_ssh_job(id: str):
    jobs_col = MongoManager.col('ssh_jobs')

    return jobs_col.find_one({'id': id})
