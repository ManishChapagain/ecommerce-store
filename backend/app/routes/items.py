from flask import Blueprint, jsonify
from app.models import store

items_bp = Blueprint("items", __name__)

@items_bp.route("/", methods=["GET"])
def get_items():
    return jsonify({"items": store.ITEMS}), 200
