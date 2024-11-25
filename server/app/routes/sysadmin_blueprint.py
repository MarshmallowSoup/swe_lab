# sysadmin_blueprint.py
from flask import Blueprint, request, jsonify
from database import db
from models import Student, Professor, UniversityAdmin, Review, SystemAdmin
from controllers  import SysAdminController

sysadmin_blueprint = Blueprint('sysadmin', __name__)

sysadmin_controller = SysAdminController()

@sysadmin_blueprint.route('/delete_user/<user_type>/<int:user_id>', methods=['DELETE'])
def delete_user(user_type, user_id):
    success = sysadmin_controller.delete_user(user_id, user_type)
    return jsonify({'success': success})

@sysadmin_blueprint.route('/validate_login_credentials', methods=['POST'])
def validate_login_credentials():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    admin = sysadmin_controller.validate_login_credentials(email, password)
    return jsonify({'admin': admin})

@sysadmin_blueprint.route('/delete_inappropriate_review/<int:review_id>', methods=['DELETE'])
def delete_inappropriate_review(review_id):
    success = sysadmin_controller.delete_inappropriate_review(review_id)
    return jsonify({'success': success})

@sysadmin_blueprint.route('/create_student', methods=['POST'])
def create_student():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    new_student = sysadmin_controller.create_student(first_name, last_name, email, password)
    return jsonify({'student': {'id': new_student.id, 'first_name': new_student.first_name, 'last_name': new_student.last_name}})

@sysadmin_blueprint.route('/create_professor', methods=['POST'])
def create_professor():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    university = data.get('university')
    password = data.get('password')
    new_professor = sysadmin_controller.create_professor(name, email, subject, university, password)
    return jsonify({'professor': {'id': new_professor.id, 'name': new_professor.name, 'email': new_professor.email}})

@sysadmin_blueprint.route('/create_university_admin', methods=['POST'])
def create_university_admin():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    university = data.get('university')
    new_admin = sysadmin_controller.create_university_admin(username, email, password, university)
    return jsonify({'admin': {'id': new_admin.id, 'username': new_admin.username, 'email': new_admin.email}})

@sysadmin_blueprint.route('/create_sysadmin', methods=['POST'])
def create_sysadmin():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    new_sysadmin = sysadmin_controller.create_sysadmin(username, email, password)
    return jsonify({'sysadmin': {'id': new_sysadmin.id, 'username': new_sysadmin.username, 'email': new_sysadmin.email}})

@sysadmin_blueprint.route('/update_sysadmin_info/<int:sysadmin_id>', methods=['PUT'])
def update_sysadmin_info(sysadmin_id):
    data = request.get_json()
    new_info = data.get('new_info')
    sysadmin = sysadmin_controller.update_sysadmin_info(sysadmin_id, new_info)
    if sysadmin:
        return jsonify({'sysadmin': {'id': sysadmin.id, 'username': sysadmin.username, 'email': sysadmin.email}})
    else:
        return jsonify({'message': 'System admin not found'})

@sysadmin_blueprint.route('/list_all_students', methods=['GET'])
def list_all_students():
    students = sysadmin_controller.list_all_students()
    student_list = [{'id': student.id, 'name': student.name, 'email': student.email} for student in students]
    return jsonify({'students': student_list})

@sysadmin_blueprint.route('/list_all_professors', methods=['GET'])
def list_all_professors():
    professors = sysadmin_controller.list_all_professors()
    professor_list = [{'id': professor.id, 'name': professor.name, 'email': professor.email} for professor in professors]
    return jsonify({'professors': professor_list})

@sysadmin_blueprint.route('/list_all_university_admins', methods=['GET'])
def list_all_university_admins():
    university_admins = sysadmin_controller.list_all_university_admins()
    admin_list = [{'id': admin.id, 'username': admin.username, 'email': admin.email} for admin in university_admins]
    return jsonify({'university_admins': admin_list})

@sysadmin_blueprint.route('/list_all_system_admins', methods=['GET'])
def list_all_system_admins():
    system_admins = sysadmin_controller.list_all_system_admins()
    sysadmin_list = [{'id': sysadmin.id, 'username': sysadmin.username, 'email': sysadmin.email} for sysadmin in system_admins]
    return jsonify({'system_admins': sysadmin_list})

@sysadmin_blueprint.route('/get_student_by_id/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    student = sysadmin_controller.get_student_by_id(student_id)
    if student:
        return jsonify({'student': {'id': student.id, 'name': student.name, 'email': student.email}})
    else:
        return jsonify({'message': 'Student not found'})

@sysadmin_blueprint.route('/get_professor_by_id/<int:professor_id>', methods=['GET'])
def get_professor_by_id(professor_id):
    professor = sysadmin_controller.get_professor_by_id(professor_id)
    if professor:
        return jsonify({'professor': {'id': professor.id, 'name': professor.name, 'email': professor.email}})
    else:
        return jsonify({'message': 'Professor not found'})

@sysadmin_blueprint.route('/get_university_admin_by_id/<int:admin_id>', methods=['GET'])
def get_university_admin_by_id(admin_id):
    admin = sysadmin_controller.get_university_admin_by_id(admin_id)
    if admin:
        return jsonify({'admin': {'id': admin.id, 'username': admin.username, 'email': admin.email}})
    else:
        return jsonify({'message': 'University admin not found'})

@sysadmin_blueprint.route('/get_system_admin_by_id/<int:sysadmin_id>', methods=['GET'])
def get_system_admin_by_id(sysadmin_id):
    sysadmin = sysadmin_controller.get_system_admin_by_id(sysadmin_id)
    if sysadmin:
        return jsonify({'sysadmin': {'id': sysadmin.id, 'username': sysadmin.username, 'email': sysadmin.email}})
    else:
        return jsonify({'message': 'System admin not found'})

if __name__ == '__main__':
    sysadmin_blueprint.run()
