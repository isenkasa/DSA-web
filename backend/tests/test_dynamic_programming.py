from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_dynamic_programming_api():
    response = client.get("/dynamic-programming/")
    assert response.status_code == 200
    assert response.json() == {"description": "Dynamic Programming API"}