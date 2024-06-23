from fastapi.testclient import TestClient

from ..schemas import ItemCategoryCreate as ItemCategoryCreateSchema
from ..models import ItemCategory as ItemCategoryModel
from .api__item_category import (
    router,
)

client = TestClient(router)


fake_db = [
    ItemCategoryCreateSchema(id=1, name="1"),
    ItemCategoryCreateSchema(id=2, name="2"),
    ItemCategoryCreateSchema(id=3, name="3"),
]


def test_create_item_category():
    response = client.post("/", json=fake_db[1].model_dump())
    assert response.status_code == 200
    model = ItemCategoryModel(**fake_db[1].model_dump())
    print(model.to_dict())
    print(response.json())
    assert response.json() == model.to_dict()


def test_read_item_categories():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [ItemCategoryModel(**x.model_dump()).to_dict() for x in fake_db]
