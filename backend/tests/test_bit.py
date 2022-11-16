from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_bit_api():
    response = client.get("/bit/")
    assert response.status_code == 200
    assert response.json() == {"description": "Bit Manipulation API"}