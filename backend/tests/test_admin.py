from app.models import store

def place_order(client, user_id="test_user", apply_code=None):
    item = {"name": "Item", "price": 100, "qty": 1}
    client.post(f"/cart/{user_id}/add", json=item)
    payload = {}
    if apply_code:
        payload["discount_code"] = apply_code
    return client.post(f"/checkout/{user_id}", json=payload)


def test_get_code_not_available(client):
    for _ in range(store.NTH_ORDER - 1):  # 3rd order
        place_order(client)
    res = client.get("/admin/get-code")
    assert res.status_code == 400
    assert res.get_json()["message"] == "Discount code not available"


def test_get_code_available(client):
    for _ in range(store.NTH_ORDER):  # 4th order 
        place_order(client)
    res = client.get("/admin/get-code")
    assert res.status_code == 200
    data = res.get_json()
    assert "code" in data
    assert data["message"] == "Discount code available"


def test_get_report(client):
    for _ in range(store.NTH_ORDER):
        place_order(client)
    
    res = client.get("/admin/report")
    data = res.get_json()

    assert res.status_code == 200
    assert data["total_items_sold"] == store.NTH_ORDER
    assert data["total_revenue"] == 100 * store.NTH_ORDER
    assert data["total_discount_given"] == 0  # No discount applied
    assert len(data["discount_codes"]) == 1 
