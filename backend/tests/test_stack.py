from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_stack_api():
    response = client.get("/stack/")
    assert response.status_code == 200
    assert response.json() == {"description": "Stack API"}