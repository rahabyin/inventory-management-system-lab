import requests

BASE_URL = "http://127.0.0.1:5000"


def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        inventory = response.json()

        if not inventory:
            print("\nInventory is empty.\n")
            return

        print("\nInventory")
        print("-" * 50)

        for item in inventory:
            print(
                f"ID: {item['id']}\n"
                f"Name: {item['name']}\n"
                f"Brand: {item['brand']}\n"
                f"Price: ${item['price']}\n"
                f"Stock: {item['stock']}\n"
            )
    else:
        print("Unable to retrieve inventory.")


def add_item():
    name = input("Product name: ")
    brand = input("Brand: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    data = {
        "name": name,
        "brand": brand,
        "price": price,
        "stock": stock
    }

    response = requests.post(f"{BASE_URL}/inventory", json=data)

    if response.status_code == 201:
        print("\nItem added successfully!\n")
    else:
        print(response.json())


def search_barcode():
    barcode = input("Barcode: ")

    response = requests.get(f"{BASE_URL}/barcode/{barcode}")

    if response.status_code == 200:
        print(response.json())
    else:
        print("Product not found.")


def search_name():
    name = input("Product name: ")

    response = requests.get(f"{BASE_URL}/search/{name}")

    if response.status_code == 200:
        products = response.json()

        for product in products:
            print(product)
    else:
        print("No products found.")


def update_item():
    item_id = input("Item ID: ")

    name = input("New name (leave blank to keep current): ")
    brand = input("New brand: ")
    price = input("New price: ")
    stock = input("New stock: ")

    data = {}

    if name:
        data["name"] = name
    if brand:
        data["brand"] = brand
    if price:
        data["price"] = float(price)
    if stock:
        data["stock"] = int(stock)

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=data
    )

    if response.status_code == 200:
        print("Item updated successfully.")
    else:
        print(response.json())


def delete_item():
    item_id = input("Item ID: ")

    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        print("Item deleted successfully.")
    else:
        print(response.json())


def main():
    while True:
        print("\nInventory Menu")
        print("-" * 20)
        print("1. View inventory")
        print("2. Add item")
        print("3. Search by barcode")
        print("4. Search by name")
        print("5. Update item")
        print("6. Delete item")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            add_item()

        elif choice == "3":
            search_barcode()

        elif choice == "4":
            search_name()

        elif choice == "5":
            update_item()

        elif choice == "6":
            delete_item()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()