from pymongo import MongoClient
from pymongo.collection import Collection

client=MongoClient()

coffees_collection : Collection = client.db.coffees