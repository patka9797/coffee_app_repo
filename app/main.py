from fastapi import FastAPI
from pymongo.cursor import Cursor  # tools for iterating in MongoDB
from bson.objectid import ObjectId
from app.models import Coffee
from app.database import coffees_collection

description="""
Coffees API helps you to choice the best coffee to you!
You can read about coffee body resulting from origin and beverage methods.

I'm sure you mathc the best beverage for you. 

If you are the coffeeholic this app is for you
"""


app = FastAPI(
 title="CoffeesAPP",
description=description,
version="0.0.1",
contact={
    "name":"Patrycja",
    "email":"patrycjamzn@gmail.com"
}  
)



@app.get("/coffees/", response_model=list[Coffee])
def get_coffees():
    coffees = []
    for coffee in coffees_collection.find():
        coffee["id"] = str(coffee["_id"])
        coffees.append(coffee)
    return coffees


@app.post("/coffees/", response_model=Coffee)
def create_coffee(coffee: Coffee):
    coffees_collection.insert_one(coffee.dict(exclude_none=True))
    return coffee


@app.delete("/coffees/{id}")
def delete_coffee(id: str):
    coffees_collection.delete_one({"_id": ObjectId(id)})
    return {f"coffee with id {id} delaited from base."}
