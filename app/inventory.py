from app.api import get_product_by_barcode

inventory = []


def add_product_by_barcode(barcode):
    product = get_product_by_barcode(barcode)

    if not product:
        return {"error": "Product not found"}

    item = {
        "barcode": barcode,
        "name": product.get("product_name", "Unknown"),
        "brand": product.get("brands", "Unknown"),
        "quantity": product.get("quantity", "Unknown")
    }

    inventory.append(item)

    return item