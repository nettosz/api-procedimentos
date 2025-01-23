from fastapi.testclient import TestClient
from app.main import app
from random import randint
client = TestClient(app)

#tests for book crud operations
id_ = randint(1, 10000)

def test_create_book():

    response = client.post("/api/v1/example/create", json={
        "id": id_,
        "name": "test book",
        "description": "test description"
    })

    assert response.status_code == 200
    assert response.json() == {
        "id": id_,
        "name": "test book",
        "description": "test description"
    }

def test_get_book():
    response = client.get(f"/api/v1/example/get/{id_}")
    assert response.status_code == 200
    assert response.json() == {
        "id": id_,
        "name": "test book",
        "description": "test description"
    }

def test_update_book():
    response = client.put(f"/api/v1/example/update/{id_}", json={
        "id": id_,
        "name": "updated book",
        "description": "updated description"
    })
    
    assert response.status_code == 200
    assert response.json() == {
        "id": id_,
        "name": "updated book",
        "description": "updated description"
    }

def test_delete_book():
    response = client.delete(f"/api/v1/example/delete/{id_}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Book deleted successfully"}
