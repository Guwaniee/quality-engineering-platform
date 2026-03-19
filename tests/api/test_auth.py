def test_login_success(client):
    res = client.post("/auth/login", json={"username": "admin", "password": "password123"})
    assert res.status_code == 200
    assert "access_token" in res.json()

def test_login_fail(client):
    res = client.post("/auth/login", json={"username": "admin", "password": "wrong"})
    assert res.status_code == 401