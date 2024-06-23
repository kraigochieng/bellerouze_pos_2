from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./test.db"
TEST_DATABASE_URL = "sqlite://"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
test_engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_test_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
