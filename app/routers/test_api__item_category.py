from fastapi.testclient import TestClient

from ..main import app
from ..schemas import ItemCategoryCreate as ItemCategoryCreateSchema

client = TestClient(app=app)

url_prefix = "/api/item_categories"


def test_create_item_category(client, override_get_db):
    mock_db_session = override_get_db
    model = ItemCategoryCreateSchema(name="1")

    # Mock the add, commit, and refresh methods
    def mock_add(instance):
        instance.id = 1  # Simulate the database assigning an ID
        return instance

    mock_db_session.add.side_effect = mock_add
    mock_db_session.commit.return_value = None
    mock_db_session.refresh.return_value = None

    response = client.post(f"{url_prefix}/", json=model.model_dump())
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"] == 1
    assert response_json["name"] == "1"

    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once()


# def test_read_item_categories():
#     response = client.get(f"{url_prefix}/")
#     assert response.status_code == 200
#     assert response.json() == [
#         ItemCategoryModel(**x.model_dump()).to_dict() for x in fake_db
#     ]
