def test_post_shop_item(client_with_test_db, test_db):
    payload = {
        "name": "Product 1",
        "rate": 9,
        "description": "This is the first product.",
        "price": 19.99,
        "image": "https://via.placeholder.com/300x200",
    }

    response = client_with_test_db.post("/api/v1/shop", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Product 1"
    assert response.json()["rate"] == 9
    assert response.json()["description"] == "This is the first product."
    assert response.json()["price"] == 19.99
    assert response.json()["image"] == "https://via.placeholder.com/300x200"
