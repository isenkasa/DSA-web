from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_graph_api():
    response = client.get("/graph/")
    assert response.status_code == 200
    assert response.json() == {"description": "Graph API"}