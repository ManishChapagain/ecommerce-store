from flask import Blueprint, jsonify
from app.models import store

admin_bp = Blueprint('admin', __name__)

@admin_bp.route("/get-code", methods=["GET"])
def get_discount_code():
    if store.ORDER_COUNTER != 0 and (store.ORDER_COUNTER + 1) % store.NTH_ORDER == 0:
        code = store.DISCOUNT_CODES[-1].get("code")
        return jsonify({"message": "Discount code available", "code": code}), 200

    return jsonify({"message": "Discount code not available"}), 400

@admin_bp.route("/report", methods=["GET"])
def get_report():
    total_items = sum(item["qty"] for order in store.ORDERS for item in order["items"])
    total_amount = sum(order["total"] for order in store.ORDERS)
    discount_amount = sum(order["discount_applied"] for order in store.ORDERS)
    codes = store.DISCOUNT_CODES
    return jsonify({
        "total_items_sold": total_items,
        "total_revenue": total_amount,
        "total_discount_given": discount_amount,
        "discount_codes": codes
    }), 200
