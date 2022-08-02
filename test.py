from flask import Flask
from flask import Blueprint

test_bp = Blueprint('test', __name__)

@test_bp.route('/test/')
def test():
    return "Hello from test Page"