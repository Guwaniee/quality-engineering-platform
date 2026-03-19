import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture()
def client():
    return TestClient(app)

@pytest.fixture()
def token(client):
    res = client.post("/auth/login", json={"username": "admin", "password": "password123"})
    assert res.status_code == 200
    return res.json()["access_token"]