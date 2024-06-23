from fastapi.testclient import TestClient

from ..schemas import ItemCategory as ItemCategorySchema
from ..models import ItemCategory as ItemCategoryModel
from .api__item_category import (
    router,
)

client = TestClient(router)


fake_db = [
    ItemCategorySchema(id=1, name="1"),
    ItemCategorySchema(id=2, name="2"),
    ItemCategorySchema(id=3, name="3"),
]


def test_create_item_category():
    response = client.post("/", json=fake_db[1].model_dump())
    assert response.status_code == 200
    model = ItemCategoryModel(**fake_db[1].model_dump())    
    assert ItemCategoryModel(**response.json()) == model


def test_read_item_categories():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [ItemCategoryModel(**x.model_dump()) for x in fake_db]
