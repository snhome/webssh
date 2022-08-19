import pymongo
import os

def connectdb():
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

def get_ssh_server(id: str):
    ser_col = MongoManager.col('ssh_servers')
    return ser_col.find_one({'id': id})

def get_ssh_job_with_server(job_id: str):
    job = get_ssh_job(job_id)
    server = get_ssh_server(job['server_id'])
    return job, server
