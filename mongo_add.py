import os
import pymongo

client = pymongo.MongoClient()
db = client.test_db
stuff = db.test_collection
print(stuff.insert_one({"hello": "world"}).inserted_id)