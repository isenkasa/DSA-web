from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_tree_api():
    response = client.get("/tree/")
    assert response.status_code == 200
    assert response.json() == {"description": "Tree API"}