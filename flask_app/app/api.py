from flask import Blueprint, jsonify
from flask_login import login_required

api = Blueprint('api', __name__)

@api.route('/')
@login_required
def hello():
    return jsonify({"message": "Hello World!"}), 200
