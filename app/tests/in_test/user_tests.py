from app.db.models import User


def test_post_user(client_with_test_db, test_db):
    payload = {
        "name": "testuser",
        "email": "testuser@example.com",
    }

    response = client_with_test_db.post("/api/v1/users", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "testuser"
    assert response.json()["email"] == "testuser@example.com"

    db_user = test_db.query(User).filter(User.email == payload["email"]).first()
    assert db_user is not None
    assert db_user.name == payload["name"]
    assert db_user.email == payload["email"]

    existing_user_payload = {
        "name": "existinguser",
        "email": "existing@example.com",
    }
    client_with_test_db.post("/api/v1/users", json=existing_user_payload)

    new_user_payload = {
        "name": "newuser",
        "email": "existing@example.com",
    }
    response = client_with_test_db.post("/api/v1/users", json=new_user_payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "User with this email already exists."


def test_get_user(client_with_test_db):
    create_response = client_with_test_db.post(
        "/api/v1/users", json={"name": "testuser", "email": "testuser@example.com"}
    )

    user_id = create_response.json()["id"]

    response = client_with_test_db.get(f"/api/v1/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "testuser"
    assert response.json()["email"] == "testuser@example.com"


def test_get_user_not_found(client_with_test_db):
    response = client_with_test_db.get("/api/v1/users/999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
