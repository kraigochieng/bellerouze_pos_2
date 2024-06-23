from fastapi.testclient import TestClient

from ..database import get_db, get_test_db, test_engine
from ..main import app
from ..models import Base
from ..models import ItemCategory as ItemCategoryModel
from ..schemas import ItemCategoryCreate as ItemCategoryCreateSchema

# from .api__item_category import (
#     router,
# )


app.dependency_overrides[get_db] = get_test_db

client = TestClient(app=app)


fake_db = [
    ItemCategoryCreateSchema(id=1, name="1"),
    ItemCategoryCreateSchema(id=2, name="2"),
    ItemCategoryCreateSchema(id=3, name="3"),
]

url_prefix = "/api/item_categories"

Base.metadata.create_all(bind=test_engine)

def test_create_item_category():
    response = client.post(f"{url_prefix}/", json=fake_db[1].model_dump())
    assert response.status_code == 200
    model = ItemCategoryModel(**fake_db[1].model_dump())
    print(model.to_dict())
    print(response.json())
    assert response.json() == model.to_dict()


def test_read_item_categories():
    response = client.get(f"{url_prefix}/")
    assert response.status_code == 200
    assert response.json() == [
        ItemCategoryModel(**x.model_dump()).to_dict() for x in fake_db
    ]
