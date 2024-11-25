# university_admin_blueprint.py
from flask import Blueprint, request, jsonify
from database import db
from models import UniversityAdmin, UniversityReview
from controllers import UniversityAdminController

university_admin_blueprint = Blueprint('university_admin', __name__)

university_admin_controller = UniversityAdminController()

@university_admin_blueprint.route('/create_university_admin', methods=['POST'])
def create_university_admin():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    university = data.get('university')

    new_admin = university_admin_controller.create_university_admin(first_name, last_name, username, email, password, university)
    
    if new_admin:
        return jsonify({'admin': {'id': new_admin.id, 'username': new_admin.username, 'email': new_admin.email}})
    else:
        return jsonify({'message': 'Failed to create university admin'})

@university_admin_blueprint.route('/get_admin_by_username/<username>', methods=['GET'])
def get_admin_by_username(username):
    admin = university_admin_controller.get_admin_by_username(username)
    
    if admin:
        return jsonify({'admin': {'id': admin.id, 'username': admin.username, 'email': admin.email}})
    else:
        return jsonify({'message': 'University admin not found'})

@university_admin_blueprint.route('/validate_login_credentials', methods=['POST'])
def validate_login_credentials():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    admin = university_admin_controller.validate_login_credentials(username, password)
    
    if admin:
        return jsonify({'admin': {'id': admin.id, 'username': admin.username, 'email': admin.email}})
    else:
        return jsonify({'message': 'Invalid credentials'})

@university_admin_blueprint.route('/create_university_review', methods=['POST'])
def create_university_review():
    data = request.get_json()
    admin_id = data.get('admin_id')
    professor_rating = data.get('professor_rating')
    course_rating = data.get('course_rating')
    professor_id = data.get('professor_id')

    new_review = university_admin_controller.create_university_review(admin_id, professor_rating, course_rating, professor_id)
    
    if new_review:
        return jsonify({'review': {'id': new_review.id, 'professor_rating': new_review.professor_rating, 'course_rating': new_review.course_rating}})
    else:
        return jsonify({'message': 'Failed to create university review'})

@university_admin_blueprint.route('/list_all_university_admins', methods=['GET'])
def list_all_university_admins():
    university_admins = university_admin_controller.list_all_university_admins()
    admin_list = [{'id': admin.id, 'username': admin.username, 'email': admin.email} for admin in university_admins]
    return jsonify({'university_admins': admin_list})

@university_admin_blueprint.route('/get_university_admin_by_id/<int:admin_id>', methods=['GET'])
def get_university_admin_by_id(admin_id):
    admin = university_admin_controller.get_university_admin_by_id(admin_id)
    
    if admin:
        return jsonify({'admin': {'id': admin.id, 'username': admin.username, 'email': admin.email}})
    else:
        return jsonify({'message': 'University admin not found'})
