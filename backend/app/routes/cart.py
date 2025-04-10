from flask import Blueprint, request, jsonify
from app.models.store import CARTS, ITEMS

cart_bp = Blueprint('cart', __name__)

@cart_bp.route("/<user_id>/add", methods=["POST"])
def add_to_cart(user_id):
    item = request.json
    item_name = item.get("name")
    qty = item.get("qty", 1)

    # Find the item by name
    matched_item = None
    for i in ITEMS:
        if i["name"].lower() == item_name.lower():
            matched_item = i
            break

    # Validate item name
    if not item_name or not matched_item:
        return jsonify({"error": "Invalid item name"}), 400
    
    # Validate qty
    if not isinstance(qty, int) or qty <= 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400
    
    # Update item in cart
    user_cart = CARTS.setdefault(user_id, [])
    for cart_item in user_cart:
        if cart_item["name"].lower() == item_name.lower():
            cart_item["qty"] += qty
            return jsonify({"message": "Item updated to cart", "cart": user_cart}), 200
    
    # If no updation, add it
    user_cart.append({
        "id": matched_item["id"],
        "name": matched_item["name"],
        "price": matched_item["price"],
        "qty": qty
    })

    return jsonify({"message": "Item added to cart", "cart": user_cart}), 200

@cart_bp.route("/<user_id>", methods=["GET"])
def get_cart(user_id):
    return jsonify(CARTS.get(user_id, [])), 200
