from fastapi.testclient import TestClient

from ..schemas import ItemCategory
from .api__item_category import (
    router,
)

client = TestClient(router)


fake_db = [
    ItemCategory(id=1, name="1"),
    ItemCategory(id=2, name="2"),
    ItemCategory(id=3, name="3"),
]


def test_create_item_category():
    response = client.post("/", json=fake_db[1].model_dump())
    assert response.status_code == 200
    assert response.json() == fake_db[1].model_dump()


def test_read_item_categories():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [x.model_dump() for x in fake_db]
