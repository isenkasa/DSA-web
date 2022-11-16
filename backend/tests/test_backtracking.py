from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_backtracking_api():
    response = client.get("/backtracking/")
    assert response.status_code == 200
    assert response.json() == {"description": "Backtracking API"}