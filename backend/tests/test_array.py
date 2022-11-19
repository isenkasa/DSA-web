from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_array_api():
    response = client.get("/array/")
    assert response.status_code == 200
    assert response.json() == {"description": "Array API"}

def test_contains_duplicate_with_dups():
    response = client.get("/array/contains-duplicate/?arr=1,2,3,4,4")
    assert response.status_code == 200
    assert response.json() == True

def test_contains_duplicate_without_dups():
    response = client.get("/array/contains-duplicate/?arr=1,2,3,4")
    assert response.status_code == 200
    assert response.json() == False