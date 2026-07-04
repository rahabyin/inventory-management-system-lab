from flask import Blueprint, jsonify

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Inventory Management API"
    })