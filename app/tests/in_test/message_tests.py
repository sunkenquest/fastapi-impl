def test_send_sms(client_with_test_db):
    payload = {"to": "+639954468804", "message": "Test message"}

    response = client_with_test_db.post("/api/v1/sms", json=payload)

    assert response.status_code == 200
