def test_create_note_missing_token(client):
    res = client.post("/notes", json={"text": "x"})
    assert res.status_code == 401

def test_create_note_empty_text(client, token):
    headers = {"Authorization": f"Bearer {token}"}
    res = client.post("/notes", json={"text": ""}, headers=headers)
    assert res.status_code == 422

def test_get_missing_note_returns_404(client, token):
    headers = {"Authorization": f"Bearer {token}"}
    res = client.get("/notes/999999", headers=headers)
    assert res.status_code == 404