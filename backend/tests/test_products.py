from fastapi.testclient import TestClient
from backend.main import app
client = TestClient(app)
import pytest
@pytest.fixture(autouse=True)
def clean_db():
    # runs before every test
    yield

client = TestClient(app)


# ----------------------------
# CREATE PRODUCT TEST
# ----------------------------
def test_create_product():
    response = client.post(
        "/products",
        json={"name": "Laptop", "price": 50000}
    )

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["name"] == "Laptop"
    assert data["price"] == 50000


# ----------------------------
# GET ALL PRODUCTS TEST
# ----------------------------
def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# ----------------------------
# GET PRODUCT BY ID TEST
# ----------------------------
def test_get_product_by_id():
    # create product first
    create_response = client.post(
        "/products",
        json={"name": "Phone", "price": 20000}
    )

    product_id = create_response.json()["id"]

    # fetch product
    response = client.get(f"/products/{product_id}")

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == product_id
    assert data["name"] == "Phone"
    assert data["price"] == 20000


# ----------------------------
# DELETE PRODUCT TEST
# ----------------------------
def test_delete_product():
    # create product first
    create_response = client.post(
        "/products",
        json={"name": "Tablet", "price": 30000}
    )

    assert create_response.status_code == 200
    product_id = create_response.json()["id"]

    # delete product
    response = client.delete(f"/products/{product_id}")

    assert response.status_code == 200, f"Got {response.status_code}: {response.text}"

    data = response.json()

    # accept multiple valid formats
    assert (
        "message" in data or "detail" in data
    )

# ----------------------------
# BASIC SMOKE TEST (API alive)
# ----------------------------
def test_api_root():
    response = client.get("/")

    assert response.status_code == 200, f"Got {response.status_code}: {response.text}"
    assert "message" in response.json()

def test_debug_routes():
    print(app.routes)
    assert len(app.routes) > 0