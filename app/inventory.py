from app.api import get_product_by_barcode

inventory = []


def add_product_by_barcode(barcode):
    product = get_product_by_barcode(barcode)

    if not product:
        return {"error": "Product not found"}

    item = {
        "id": inventory[-1]["id"] + 1 if inventory else 1,
        "name": product.get("product_name", "Unknown"),
        "brand": product.get("brands", "Unknown"),
        "price": 0.0,
        "stock": 1,
        "barcode": barcode
    }

    inventory.append(item)

    return item