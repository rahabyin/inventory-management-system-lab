# Inventory Management System

## Overview

The Inventory Management System is a Flask-based REST API with a Command Line Interface (CLI) for managing inventory items. It allows users to create, retrieve, update, and delete inventory records while demonstrating RESTful API development, Flask routing, JSON handling, API integration, and testing.

---

## Features

* View all inventory items
* View a single inventory item
* Add new inventory items
* Update existing inventory items
* Delete inventory items
* Search products by barcode (OpenFoodFacts API)
* Search products by product name (OpenFoodFacts API)
* Command Line Interface (CLI)
* REST API using Flask
* Unit tests using pytest

---

## Project Structure

```text
inventory-management-system/
│
├── app
│   ├── __init__.py
│   ├── api.py
│   ├── inventory.py
│   └── routes.py
│
├── cli
│   ├── __init__.py
│   └── menu.py
│
├── data
│   ├── __init__.py
│   └── inventory_data.py
│
├── tests
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_cli.py
│   └── test_routes.py
│
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python 3
* Flask
* Requests
* Pytest
* Git
* GitHub

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd inventory-management-system
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment.

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Flask Application

Start the development server:

```bash
python run.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

---

## Running the CLI

Open a second terminal while the Flask server is running.

Run:

```bash
python cli/menu.py
```

Menu:

```text
Inventory Menu
--------------
1. View inventory
2. Add item
3. Search by barcode
4. Search by name
5. Update item
6. Delete item
7. Exit
```

---

## API Endpoints

| Method | Endpoint                   | Description                     |
| ------ | -------------------------- | ------------------------------- |
| GET    | `/`                        | Welcome message                 |
| GET    | `/inventory`               | Retrieve all inventory items    |
| GET    | `/inventory/<id>`          | Retrieve a single item          |
| POST   | `/inventory`               | Add a new item                  |
| PATCH  | `/inventory/<id>`          | Update an item                  |
| DELETE | `/inventory/<id>`          | Delete an item                  |
| GET    | `/barcode/<barcode>`       | Search product by barcode       |
| GET    | `/search/<name>`           | Search products by name         |
| POST   | `/inventory/add/<barcode>` | Add a product using its barcode |

---

## Example JSON

Create an inventory item:

```json
{
  "name": "Organic Almond Milk",
  "brand": "Silk",
  "price": 4.99,
  "stock": 15
}
```

Example response:

```json
{
  "id": 1,
  "name": "Organic Almond Milk",
  "brand": "Silk",
  "price": 4.99,
  "stock": 15
}
```

---

## Running Tests

Run all tests:

```bash
python -m pytest
```

or

```bash
pytest
```

---

## Known Limitations

* Product search by barcode and name depends on the OpenFoodFacts API.
* If the external API is unavailable or returns a `403 Forbidden` response, barcode and product search features may not function until access is restored.

---

## Future Improvements

* Persistent database storage using SQLite or PostgreSQL.
* User authentication and authorization.
* Product image support.
* Inventory categories.
* Pagination and filtering.
* Improved error handling and logging.
* Docker deployment.

---

## Author

Rahab Wanja

---

## License

This project was developed for educational purposes.
