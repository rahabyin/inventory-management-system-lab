from flask import Blueprint, jsonify, request
from data.inventory_data import inventory
from app.api import (
    get_product_by_barcode,
    search_products
)
from app.inventory import add_product_by_barcode

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

@inventory_bp.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    required_fields = ["name", "brand", "price", "stock"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    new_item = {
        "id": inventory[-1]["id"] + 1 if inventory else 1,
        "name": data["name"],
        "brand": data["brand"],
        "price": data["price"],
        "stock": data["stock"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

@inventory_bp.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()

    for key in ["name", "brand", "price", "stock"]:
        if key in data:
            item[key] = data[key]

    return jsonify(item), 200

@inventory_bp.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    inventory.remove(item)

    return jsonify({"message": "Item deleted successfully"}), 200

@inventory_bp.route("/barcode/<barcode>")
def barcode_lookup(barcode):

    product = get_product_by_barcode(barcode)

    if not product:
        return {
            "error": "Product not found"
        }, 404

    return {
        "barcode": barcode,
        "name": product.get("product_name"),
        "brand": product.get("brands"),
        "quantity": product.get("quantity")
    }

@inventory_bp.route("/search/<name>")
def search(name):

    products = search_products(name)

    results = []

    for product in products[:10]:
        results.append({
            "name": product.get("product_name"),
            "barcode": product.get("code"),
            "brand": product.get("brands")
        })

    return results

@inventory_bp.route("/inventory/add/<barcode>", methods=["POST"])
def add_inventory_item(barcode):
    item = add_product_by_barcode(barcode)

    if "error" in item:
        return item, 404

    return item, 201