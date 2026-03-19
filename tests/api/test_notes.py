def test_create_and_get_note(client, token):
    headers = {"Authorization": f"Bearer {token}"}

    create = client.post("/notes", json={"text": "hello"}, headers=headers)
    assert create.status_code == 200
    note_id = create.json()["id"]

    get_note = client.get(f"/notes/{note_id}", headers=headers)
    assert get_note.status_code == 200
    assert get_note.json()["text"] == "hello"

def test_delete_note(client, token):
    headers = {"Authorization": f"Bearer {token}"}

    create = client.post("/notes", json={"text": "to delete"}, headers=headers)
    note_id = create.json()["id"]

    delete = client.delete(f"/notes/{note_id}", headers=headers)
    assert delete.status_code == 200
    assert delete.json()["deleted"] is True