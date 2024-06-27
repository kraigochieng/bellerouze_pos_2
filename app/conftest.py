import pytest
from .database import get_db
from .main import app
from unittest.mock import MagicMock
from fastapi.testclient import TestClient

@pytest.fixture()
def override_get_db():
    mock_db_session = MagicMock()    
    yield mock_db_session
    mock_db_session.close()

@pytest.fixture()
def client(override_get_db):
    app.dependency_overrides[get_db] = lambda: override_get_db
    with TestClient(app) as client:
        yield client

# @pytest.fixture(scope="module", autouse=True)
# def setup_and_teardown():
#     app.dependency_overrides[get_db] = override_get_db
#     # Create tables before tests
#     # Base.metadata.create_all(bind=test_engine)
#     yield
#     # Clean up tables after tests
#     # Base.metadata.drop_all(bind=test_engine)


# app.dependency_overrides[get_db] = lambda: override_get_db
