def test_get_items(client):
    response = client.get("/items/")
    assert response.status_code == 200

    data = response.get_json()
    assert "items" in data
    assert isinstance(data["items"], list)

    for item in data["items"]:
        assert "id" in item
        assert "name" in item
        assert "price" in item
