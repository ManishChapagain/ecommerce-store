import pytest
from app.models import store

@pytest.fixture
def user_id():
    return "user123"

def test_checkout_without_cart(client, user_id):
    response = client.post(f"/checkout/{user_id}")
    assert response.status_code == 400
    assert response.json["error"] == "Cart is empty"

def test_checkout_without_discount(client, user_id):
    # Add items to cart
    store.CARTS[user_id] = [
        {"name": "Shirt", "price": 25, "qty": 2},
        {"name": "Jeans", "price": 40, "qty": 1},
    ]

    response = client.post(f"/checkout/{user_id}", json={})
    assert response.status_code == 200
    assert response.json["message"] == "Order placed"
    assert store.ORDER_COUNTER == 1
    assert len(store.ORDERS) == 1
    assert store.CARTS[user_id] == []

def test_checkout_with_valid_discount(client, user_id):
    # Set up order to be 4th (discount valid)
    store.ORDER_COUNTER = 3
    discount_code = "SAVE10"
    store.DISCOUNT_CODES.append({"code": discount_code, "used": False})

    store.CARTS[user_id] = [
        {"name": "Shoes", "price": 50, "qty": 2}
    ]

    response = client.post(f"/checkout/{user_id}", json={"discount_code": discount_code})
    assert response.status_code == 200
    assert response.json["message"] == "Order placed"
    assert store.DISCOUNT_CODES[-1]["used"] is True
    assert store.ORDER_COUNTER == 4
    assert len(store.ORDERS) == 1

def test_checkout_with_invalid_code(client, user_id):
    store.ORDER_COUNTER = 3
    store.DISCOUNT_CODES.append({"code": "VALID10", "used": False})

    store.CARTS[user_id] = [{"name": "Bag", "price": 60, "qty": 1}]

    response = client.post(f"/checkout/{user_id}", json={"discount_code": "INVALID10"})
    assert response.status_code == 400
    assert response.json["error"] == "Invalid discount code"

def test_checkout_with_used_code(client, user_id):
    store.ORDER_COUNTER = 3
    store.DISCOUNT_CODES.append({"code": "USED10", "used": True})

    store.CARTS[user_id] = [{"name": "Cap", "price": 20, "qty": 2}]

    response = client.post(f"/checkout/{user_id}", json={"discount_code": "USED10"})
    assert response.status_code == 400
    assert response.json["error"] == "Discount code already used"
