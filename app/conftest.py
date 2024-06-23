import pytest
from .database import Base, test_engine

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # Create tables before tests
    Base.metadata.create_all(bind=test_engine)
    yield
    # Clean up tables after tests
    Base.metadata.drop_all(bind=test_engine)