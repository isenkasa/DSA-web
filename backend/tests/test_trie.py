from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_trie_api():
    response = client.get("/trie/")
    assert response.status_code == 200
    assert response.json() == {"description": "Trie API"}