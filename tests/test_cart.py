def test_add_item_to_cart(client):
    response = client.post("/cart/test_user/add", json={
        "name": "apple",
        "qty": 2,
        "price": 3
    })
    assert response.status_code == 200
    assert response.get_json()["message"] == "Item added to cart"

def test_get_cart_with_items(client):
    client.post("/cart/test_user/add", json={
        "name": "banana",
        "qty": 1,
        "price": 2.5
    })

    response = client.get("/cart/test_user")
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert data[0]["name"] == "banana"
    assert data[0]["qty"] == 1
    assert data[0]["price"] == 2.5

def test_get_cart_empty(client):
    response = client.get("/cart/unknown_user")
    assert response.status_code == 200
    assert response.get_json() == []
