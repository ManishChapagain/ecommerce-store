def test_add_item_to_cart(client):
    response = client.post("/cart/test_user/add", json={
        "name": "apple",
        "qty": 2
    })
    assert response.status_code == 200
    assert response.get_json()["message"] == "Item added to cart"

def test_update_existing_item_in_cart(client):
    client.post("/cart/test_user/add", json={
        "name": "Apple",
        "qty": 2
    })
    response = client.post("/cart/test_user/add", json={
        "name": "Apple",
        "qty": 3
    })
    assert response.status_code == 200
    assert response.get_json()["message"] == "Item updated to cart"

    cart_response = client.get("/cart/test_user")
    cart = cart_response.get_json()
    assert cart[0]["name"].lower() == "apple"
    assert cart[0]["qty"] == 5

def test_add_invalid_item_name(client):
    response = client.post("/cart/test_user/add", json={
        "name": "InvalidItem",
        "qty": 1
    })
    assert response.status_code == 400
    assert "Invalid item name" in response.get_json()["error"]

def test_add_invalid_quantity(client):
    response = client.post("/cart/test_user/add", json={
        "name": "Apple",
        "qty": -2
    })
    assert response.status_code == 400
    assert "Quantity must be a positive integer" in response.get_json()["error"]

def test_get_cart_with_items(client):
    client.post("/cart/test_user/add", json={
        "name": "banana",
        "qty": 1
    })

    response = client.get("/cart/test_user")
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert data[0]["name"].lower() == "banana"
    assert data[0]["qty"] == 1
    assert data[0]["price"] == 5

def test_get_cart_empty(client):
    response = client.get("/cart/unknown_user")
    assert response.status_code == 200
    assert response.get_json() == []
