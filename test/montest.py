from pymongo import MongoClient
client = MongoClient('localhost',username='user',password='pa',authSource='test')

db = client['test']
collect = db['restaurants']

for ele in collect.find():
    print(ele)