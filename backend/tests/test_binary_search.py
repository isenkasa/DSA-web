from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_binary_search_api():
    response = client.get("/binary-search/")
    assert response.status_code == 200
    assert response.json() == {"description": "Binary Search API"}