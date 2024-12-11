from fastapi.testclient import TestClient
import pytest  # type: ignore
from app.db.connection import get_db, get_test_db, Base, test_engine
from app.main import app
from sqlalchemy.orm import sessionmaker

app.dependency_overrides[get_db] = get_test_db

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="function")
def test_db():
    """Fixture to provide a clean database for each test."""
    Base.metadata.create_all(bind=test_engine)

    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="function")
def override_db_dependency(test_db):
    """Fixture to override the app's database dependency for testing."""
    app.dependency_overrides[get_db] = get_test_db
    yield
    app.dependency_overrides.clear()


@pytest.fixture
def client_with_test_db(override_db_dependency):
    """Fixture for TestClient using the test database."""
    from app.main import app

    with TestClient(app) as test_client:
        yield test_client
