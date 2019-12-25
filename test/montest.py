from pymongo import MongoClient
client = MongoClient('localhost',username='user',password='pa',authSource='project')

db = client['project']
users = db['users']

user = users.find_one({"id" : "admin"})

bookName = "測試"

# print(user["books"])

if bookName not in user["books"]:
    print("no")
else:

    books = db["books"]
    pages = db["pages"]

    theBook = books.find_one({"name" : bookName})

    maxPage = theBook["maxPage"]

    thePages = pages.find_one({"bookName" : bookName, "number": 1})

    # for ele in thePages:
    #     print(ele["pageName"])

    print(thePages)
