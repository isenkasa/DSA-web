from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"description": "Data Structures and Algorithms API"}
