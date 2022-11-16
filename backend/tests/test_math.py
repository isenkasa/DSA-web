from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_math_api():
    response = client.get("/math/")
    assert response.status_code == 200
    assert response.json() == {"description": "Math API"}