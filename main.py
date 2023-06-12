from fastapi import FastAPI
from pymongo.cursor import Cursor  # tools for iterating in MongoDB
from bson.objectid import ObjectId
from app.models import Coffee
from app.database import coffees_collection


app = FastAPI()


@app.get("/coffees/", response_model=list[Coffee])
def get_coffees():
    coffees: Cursor = coffees_collection.find()
    coffees_models = []
    for coffee in coffees:
        coffee["id"] = str(coffee["_id"])
        coffees_models.append(coffee)
    return coffees_models


@app.post("/coffees", response_model=Coffee)
def create_coffes(coffee: Coffee):
    coffees_collection.insert_one(coffee.dict(exclude_none=True))
    return coffee


@app.get("/coffees")
def description(string):
    string = """"
    This API helps ypu to find perfect kind of coffee.
    API gives you all details you need to make perfect beverge.
    What can I sai? Hm... Enjoj!!!
    """
    print(string)
