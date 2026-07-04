from flask import Blueprint

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/")
def home():
    return {
        "message": "Welcome to the Inventory Management API"
    }
