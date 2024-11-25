from flask import Blueprint, request, jsonify
from controllers import StudentController

# Create a Blueprint instance

# Initialize the StudentController
student_controller = StudentController()
# Create a Blueprint instance
student_blueprint = Blueprint('student', __name__)

# Route to create a new student
@student_blueprint.route('/create', methods=['POST'])
def create_student():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    result = student_controller.create_student(first_name, last_name, email, password)
    
    if isinstance(result, str):
        return jsonify({'error': result}), 400

    return jsonify({'message': 'Student created successfully', 'student_id': result.id}), 201

# Route to get student reviews
@student_blueprint.route('/<int:student_id>/reviews', methods=['GET'])
def get_student_reviews(student_id):
    reviews = student_controller.get_student_reviews(student_id)
    return jsonify({'reviews': [review.serialize() for review in reviews]})

# Route to edit student profile
@student_blueprint.route('/<int:student_id>/edit', methods=['PUT'])
def edit_student_profile(student_id):
    data = request.json
    result = student_controller.edit_student_profile(student_id, data)

    if result:
        return jsonify({'message': 'Student profile updated successfully'})
    else:
        return jsonify({'error': 'Student not found'}), 404

# Route to change student password
@student_blueprint.route('/<int:student_id>/change-password', methods=['PUT'])
def change_student_password(student_id):
    data = request.json
    new_password = data.get('new_password')

    result = student_controller.change_password(student_id, new_password)

    if result:
        return jsonify({'message': 'Student password changed successfully'})
    else:
        return jsonify({'error': 'Student not found'}), 404

# Route to submit a review
@student_blueprint.route('/submit-review', methods=['POST'])
def submit_review():
    data = request.json
    student_id = data.get('student_id')
    professor_id = data.get('professor_id')
    rating = data.get('rating')
    comment = data.get('comment')
    anonymous = data.get('anonymous')

    result = student_controller.submit_review(student_id, professor_id, rating, comment, anonymous)

    return jsonify({'message': 'Review submitted successfully', 'review_id': result.id}), 201

# Route to get professor details
@student_blueprint.route('/professor/<int:professor_id>', methods=['GET'])
def get_professor_details(professor_id):
    result = student_controller.get_professor_details(professor_id)

    if result:
        return jsonify(result.serialize())
    else:
        return jsonify({'error': 'Professor not found'}), 404

# Route to validate login credentials
@student_blueprint.route('/login', methods=['POST'])
def validate_login_credentials():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    student = student_controller.validate_login_credentials(email, password)

    if student:
        return jsonify({'message': 'Login successful', 'student_id': student.id})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Route to get a student by ID
@student_blueprint.route('/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    result = student_controller.get_student_by_id(student_id)

    if result:
        return jsonify(result.serialize())
    else:
        return jsonify({'error': 'Student not found'}), 404

# Route to list all students
@student_blueprint.route('/list', methods=['GET'])
def list_all_students():
    students = student_controller.list_all_students()
    return jsonify({'students': [student.serialize() for student in students]})

# Add more routes as needed

# ...

