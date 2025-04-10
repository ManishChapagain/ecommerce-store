import pytest
from flask import Flask
from app.routes.cart import cart_bp
from app.routes.checkout import checkout_bp
from app.routes.admin import admin_bp
from app.models import store

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(cart_bp, url_prefix="/cart")
    app.register_blueprint(checkout_bp, url_prefix="/checkout")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def clear_cart_store():
    # clear the cart store before each test
    store.CARTS.clear()
    store.ORDERS.clear()
    store.DISCOUNT_CODES.clear()
    store.ORDER_COUNTER = 0
