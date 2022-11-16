from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_interval_api():
    response = client.get("/interval/")
    assert response.status_code == 200
    assert response.json() == {"description": "Interval API"}