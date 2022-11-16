from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_heap_api():
    response = client.get("/heap/")
    assert response.status_code == 200
    assert response.json() == {"description": "Heap API"}