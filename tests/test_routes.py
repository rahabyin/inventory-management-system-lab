import pytest
from app import create_app
from data.inventory_data import inventory


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_add_item(client):
    new_item = {
        "name": "Rice",
        "brand": "Sunrice",
        "price": 5.99,
        "stock": 10
    }

    response = client.post("/inventory", json=new_item)

    assert response.status_code == 201
    assert response.get_json()["name"] == "Rice"


def test_get_single_item(client):
    response = client.get("/inventory/1")
    assert response.status_code == 200


def test_delete_item(client):
    response = client.delete("/inventory/1")
    assert response.status_code == 200