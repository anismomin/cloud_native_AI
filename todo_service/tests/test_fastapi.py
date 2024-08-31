from fastapi.testclient import TestClient

from src.fastapi import app

def test_root_path():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_items_path():
    client = TestClient(app)
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}