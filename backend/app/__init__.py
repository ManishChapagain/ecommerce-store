from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes.cart import cart_bp
    from .routes.checkout import checkout_bp
    from .routes.admin import admin_bp
    from .routes.items import items_bp

    app.register_blueprint(items_bp, url_prefix="/items")
    app.register_blueprint(cart_bp, url_prefix="/cart")
    app.register_blueprint(checkout_bp, url_prefix="/checkout")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    return app
