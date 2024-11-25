from flask import Blueprint, request, jsonify, current_app
from flask_login import login_required
from controllers import AuthController

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login', methods=['POST'])
def login():
    auth_controller = current_app.config['auth_controller']

    data = request.get_json()
    user_type = data.get('user_type')
    email = data.get('email')
    password = data.get('password')

    if auth_controller.login(user_type=user_type, email=email, password=password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Login failed'}), 401

@auth_blueprint.route('/register', methods=['POST'])
def register():
    auth_controller = current_app.config['auth_controller']
    data = request.get_json()
    user_type = data.get('user_type')
    email = data.get('email')
    password = data.get('password')
    kwargs = data.get('kwargs', {})

    auth_controller.register(user_type, email, password, **kwargs)

    return jsonify({'message': 'Registration successful'}), 200

@auth_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    auth_controller = current_app.config['auth_controller']
    auth_controller.logout()
    return jsonify({'message': 'Logout successful'}), 200

@auth_blueprint.route('/current_user', methods=['GET'])
@login_required
def get_current_user():
    auth_controller = current_app.config['auth_controller']
    current_user = auth_controller.get_current_user()
    # You may want to serialize 'current_user' to JSON or return specific data
    return jsonify({'username': current_user.username, 'user_type': current_user.user_type}), 200
