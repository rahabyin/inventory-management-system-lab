from flask import Blueprint, jsonify, request
from data.inventory_data import inventory

inventory_bp = Blueprint("inventory", __name__)