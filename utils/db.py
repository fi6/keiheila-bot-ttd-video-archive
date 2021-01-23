from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient('localhost', 27017)
db = client.test_db
archives: Collection = db.archives
subscribes: Collection = db.subscribes