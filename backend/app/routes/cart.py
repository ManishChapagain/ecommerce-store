from flask import Blueprint, request, jsonify
from app.models.store import CARTS

cart_bp = Blueprint('cart', __name__)

@cart_bp.route("/<user_id>/add", methods=["POST"])
def add_to_cart(user_id):
    # todo: add validation
    item = request.json
    CARTS.setdefault(user_id, []).append(item)
    return jsonify({"message": "Item added to cart"}), 200

@cart_bp.route("/<user_id>", methods=["GET"])
def get_cart(user_id):
    return jsonify(CARTS.get(user_id, [])), 200
