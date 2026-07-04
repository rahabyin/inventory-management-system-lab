from flask import Blueprint, jsonify, request
from data.inventory_data import inventory

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Inventory Management API"
    })

@inventory_bp.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200

@inventory_bp.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200