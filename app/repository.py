from abc import ABC, abstractmethod
from uuid import uuid4

from bson import ObjectId
from pymongo import CursorType
from pymongo.collection import Collection
from app.exeptions import CoffeeNotFounf
from app.models import Coffee


class Repository(ABC):
    @abstractmethod
    def get_coffees(self, id: str):
        ...

    @abstractmethod
    def created_coffee(self, coffee: Coffee):
        ...

    @abstractmethod
    def deleted_coffee(self, id: str):
        ...

    class InMemoryRepository(Repository):
        def __init__(self):
            self.collection = []

        def _get_next_id(self):
            return uuid4()

    class MongoRepository(Repository):
        def __init__(self, coffees_collection: Collection):
            self._coffees_collecion = coffees_collection

    def get_coffees(self):
        coffees: CursorType = self._coffees_collection.find()
        coffees = []
        for coffee in self.coffees_collection.find():
            coffee["id"] = str(coffee["_id"])
            coffees.append(coffee)
        return coffees
        raise CoffeeNotFounf(f"Coffee with id '{id}' not found. Try again")

    def create_coffee(self, coffee: Coffee):
        coffee_id = self._coffees_collection.insert_one(coffee.dict(exclude_none=True))
        coffee.id = str(coffee_id.inserted_id)
        return coffee

    def delete_coffee(self, id: str):
        self._coffees_collection.delete_one({"_id": ObjectId(id)})

        return {f"coffee with id {id} delaited from base."}
