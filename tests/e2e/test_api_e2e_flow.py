import requests

BASE = "http://127.0.0.1:8000"

def test_api_e2e_login_create_get_delete():
    # login
    r = requests.post(f"{BASE}/auth/login", json={"username": "admin", "password": "password123"})
    assert r.status_code == 200
    token = r.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # create
    c = requests.post(f"{BASE}/notes", json={"text": "e2e note"}, headers=headers)
    assert c.status_code == 200
    note_id = c.json()["id"]

    # get
    g = requests.get(f"{BASE}/notes/{note_id}", headers=headers)
    assert g.status_code == 200
    assert g.json()["text"] == "e2e note"

    # delete
    d = requests.delete(f"{BASE}/notes/{note_id}", headers=headers)
    assert d.status_code == 200
    assert d.json()["deleted"] is True
