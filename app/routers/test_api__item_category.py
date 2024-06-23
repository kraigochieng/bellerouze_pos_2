from fastapi.testclient import TestClient

from ..database import get_db, override_get_db
from ..main import app
from ..models import ItemCategory as ItemCategoryModel
from ..schemas import ItemCategoryCreate as ItemCategoryCreateSchema

# from .api__item_category import (
#     router,
# )


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app=app)


fake_db = [
    ItemCategoryCreateSchema(id=1, name="1").model_dump(),
    ItemCategoryCreateSchema(id=2, name="2").model_dump(),
    ItemCategoryCreateSchema(id=3, name="3").model_dump(),
]

print(f"{fake_db=}")
url_prefix = "/api/item_categories"


def test_create_item_category():
    response = client.post(f"{url_prefix}/", json=fake_db[1])
    assert response.status_code == 200
    model = ItemCategoryModel(**fake_db[1])
    print(model.to_dict())
    print(response.json())
    assert response.json() == model.to_dict()


def test_read_item_categories():
    response = client.get(f"{url_prefix}/")
    assert response.status_code == 200
    assert response.json() == [
        ItemCategoryModel(**x.model_dump()).to_dict() for x in fake_db
    ]
