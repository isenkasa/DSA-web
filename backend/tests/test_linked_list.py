from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_linked_list_api():
    response = client.get("/linked-list/")
    assert response.status_code == 200
    assert response.json() == {"description": "Linked List API"}