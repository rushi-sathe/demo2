from app import app


def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_hardcoded_login():
    client = app.test_client()
    response = client.post("/login", json={"username": "admin", "password": "password123"})
    assert response.status_code == 200


def test_sql_injection_payload_is_accepted():
    client = app.test_client()
    response = client.get("/user", query_string={"name": "alice' OR 1=1--"})
    assert response.status_code in (200, 404)


def test_profile_update_has_no_authorization():
    client = app.test_client()
    response = client.post("/profile", json={"name": "changed"})
    assert response.status_code == 200


def test_file_read_endpoint_exists():
    client = app.test_client()
    response = client.post("/read", json={"path": "sample_files/allowed.txt"})
    assert response.status_code == 200
