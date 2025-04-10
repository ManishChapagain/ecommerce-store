from flask import Blueprint, request, jsonify
from app.models import store
import random, string

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route("/<user_id>", methods=["POST"])
def checkout(user_id):
    # todo: add validation
    cart = store.CARTS.get(user_id, [])
    if not cart:
        return jsonify({"error": "Cart is empty"}), 400
    
    current_order_number = store.ORDER_COUNTER + 1
    current_discount_code = request.json.get("discount_code")
    subtotal = sum(item["price"] * item["qty"] for item in cart)
    discount = 0

    # Check if current order is Nth and given discount code is valid (if given)
    if current_discount_code:
        if current_order_number % store.NTH_ORDER == 0:
            last_available_code = store.DISCOUNT_CODES[-1]
            if last_available_code["code"] == current_discount_code and not last_available_code["used"]:
                discount = 0.10 * subtotal
                last_available_code["used"] = True
            elif last_available_code["code"] == current_discount_code and last_available_code["used"]:
                return jsonify({"error": "Discount code already used"}), 400
            else:
                return jsonify({"error": "Invalid discount code"}), 400
        else:
            return jsonify({"error": "Cannot apply discount code"}), 400

    total = subtotal - discount

    # Record order
    store.ORDER_COUNTER = current_order_number
    store.ORDERS.append({
        "user_id": user_id,
        "items": cart,
        "subtotal": subtotal,
        "discount_applied": discount,
        "total": total
    })

    # Clear cart
    store.CARTS[user_id] = []

    # Generate discount code if next order is Nth
    if (current_order_number + 1) % store.NTH_ORDER == 0:
        new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        store.DISCOUNT_CODES.append({"code": new_code, "used": False})

    return jsonify({"message": "Order placed", "total": total}), 200
