from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./fastapi.db"
TEST_DATABASE_URL = "sqlite:///./fastapi_test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
test_engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

Base = declarative_base()


def get_db():
    """Database dependency for the app."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_test_db():
    """Database dependency for tests."""
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
