import pymongo
import os
from dotenv import load_dotenv
from nanoid import generate
from datetime import datetime, timedelta

load_dotenv()  # take environment variables from .env.

db_url = os.environ.get("DATABASE_URL")
print(db_url)
myclient = pymongo.MongoClient(db_url)
mydb = myclient["webssh"]

ssh_servers = mydb["ssh_servers"]
ssh_servers.create_index('id', unique=True)

home_server_dict = {"hostname": "192.168.1.145", "port":22, "username": "root", "password": "", 'id': 'home-145', 'agent': True }

try:
  x = ssh_servers.insert_one(home_server_dict)
except Exception as e:
  print(e)

ssh_jobs = mydb["ssh_jobs"]
ssh_jobs.create_index('id', unique=True)

jobid = generate(size=11)
now = datetime.now()
exp = int(datetime.timestamp(now + timedelta(hours=180)))
print(exp)
job_dict = { 'exp': exp, 'secret': '8899', 'command': 'echo hi\nsleep 2\necho done', 'id': jobid, 'server_id': home_server_dict['id']}
x = ssh_jobs.insert_one(job_dict)

job = ssh_jobs.find_one({'id':jobid})
server = ssh_servers.find_one({'id': job['server_id']})

print(server['hostname'])
print(job)

