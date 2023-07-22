import string

import pytest
from pydantic_factories import ModelFactory
from test.conftest import CoffeeFactory

from app.exceptions import CoffeeNotFound
from app.models import Coffee
from app.repository import  MongoRepository


@pytest.ficture()
def repository()-> MongoRepository:
    collection = [CoffeeFactory.build(id=id) for id in string.ascii_lowercase]
    return MongoRepository(collection)

class TestMongoRepository:
    def test_get_coffees__coffes_found(self, repository):
        id ='a'

        result=repository.get_coffees(id)

        assert isinstance(result, Coffee)
        assert result.id==id

    def test_get_coffees_coffees_not_founr(self, repostory):
        id = 'A'

        with pytest.rise(CoffeeNotFound) as exc_info:
            repository.get_coffees(id)

        assert str(exc_info.value)=="Coffee with id '{id}' not found. Try again"
    def test_create_coffee(self, repository):
        coffee=CoffeeFactory.bulid(id='a')

        result = repository.create_coffee(coffee)

        assert result == coffee
    
                                