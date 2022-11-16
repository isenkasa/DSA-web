from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_greedy_api():
    response = client.get("/greedy/")
    assert response.status_code == 200
    assert response.json() == {"description": "Greedy Algorithms API"}