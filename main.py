from fastapi import FastAPI
from pymongo.cursor import Cursor #tools for iterating in MongoDB
from bson.objectid import ObjectId
from models import Coffee
from database import coffees_collection


app= FastAPI()
 
@app.get("/coffees/", response_model=list[Coffee])
def get_coffees():
    coffees: Cursor = coffees_collection.find()
    coffees_models=[]
    for coffee in coffees: 
        coffee['id']= str(coffee['_id'])
        coffees_models.append(coffee)
    return coffees_models

