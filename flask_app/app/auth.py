from flask import Blueprint, request, jsonify
from flask_login import login_user, login_required, logout_user
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing request data"}), 400

    username = data.get('username')

    if not username:
        return jsonify({"error": "Missing username"}), 400

    user = User.get_by_username(username)

    if not user :
        return jsonify({"error": "Invalid username"}), 401

    login_user(user)

    return jsonify({"message": "Logged in successfully"}), 200

@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200
