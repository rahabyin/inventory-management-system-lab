from flask import Flask
from app.routes import inventory_bp

def create_app():
    app = Flask(__name__)

    from app.routes import inventory_bp
    app.register_blueprint(inventory_bp)

    return app