import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["mydatabase"]
mycool = mydb["customers"]

print(mydb.list_collection_names())