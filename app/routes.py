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
