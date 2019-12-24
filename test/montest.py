from pymongo import MongoClient
client = MongoClient('localhost',username='user',password='pa',authSource='project')

db = client['project']
users = db['users']

man = users.find_one({ "id" : "ad" })

print(man)