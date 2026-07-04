import requests

BASE_URL = "https://world.openfoodfacts.org/api/v2"

HEADERS = {
    "User-Agent": "InventoryManagementSystem/1.0 (learning project)"
}


def get_product_by_barcode(barcode):
    url = f"{BASE_URL}/product/{barcode}.json"

    response = requests.get(url, headers=HEADERS)

    print("Status code:", response.status_code)
    print("Response:")
    print(response.text)

    if response.status_code != 200:
        return None

    data = response.json()

    print("JSON:")
    print(data)

    if data.get("status") == 0:
        return None

    return data.get("product")

def search_products(name):
    url = "https://world.openfoodfacts.org/cgi/search.pl"

    params = {
        "search_terms": name,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }

    response = requests.get(url, params=params, headers=HEADERS)

    if response.status_code != 200:
        print("Status:", response.status_code)
        return []

    data = response.json()

    return data.get("products", [])