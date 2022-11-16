from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_string_api():
    response = client.get("/string/")
    assert response.status_code == 200
    assert response.json() == {"description": "String API"}