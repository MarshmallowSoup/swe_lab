from flask import Blueprint, jsonify, request
from models import Professor
from controllers import ProfessorController

professor_blueprint = Blueprint('professor', __name__)

professor_controller = ProfessorController()

@professor_blueprint.route('/<int:professor_id>', methods=['GET'])
def get_professor_by_id(professor_id):
    professor = professor_controller.get_professor_by_id(professor_id)

    if professor:
        return jsonify(professor.serialize())
    else:
        return jsonify({'error': 'Professor not found'}), 404

@professor_blueprint.route('/<int:professor_id>/reviews', methods=['GET'])
def get_professor_reviews(professor_id):
    reviews = professor_controller.get_professor_reviews(professor_id)
    serialized_reviews = [review.serialize() for review in reviews]

    return jsonify({'reviews': serialized_reviews})

@professor_blueprint.route('/list', methods=['GET'])
def list_all_professors():
    professors = professor_controller.list_all_professors()
    serialized_professors = [professor.serialize() for professor in professors]

    return jsonify({'professors': serialized_professors})

@professor_blueprint.route('/create', methods=['POST'])
def create_professor():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    subject = data.get('subject')
    university = data.get('university')

    new_professor = professor_controller.create_professor(name, email, password, subject, university)
    
    return jsonify(new_professor.serialize()), 201

@professor_blueprint.route('/<int:professor_id>/update', methods=['PUT'])
def update_professor_info(professor_id):
    data = request.get_json()
    updated_professor = professor_controller.update_professor_info(professor_id, data)

    if updated_professor:
        return jsonify(updated_professor.serialize())
    else:
        return jsonify({'error': 'Professor not found'}), 404

@professor_blueprint.route('/login', methods=['POST'])
def validate_login_credentials():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    professor = professor_controller.validate_login_credentials(email, password)

    if professor:
        return jsonify(professor.serialize())
    else:
        return jsonify({'error': 'Invalid login credentials'}), 401

@professor_blueprint.route('/<int:review_id>/submit_answer', methods=['PUT'])
def submit_answer(review_id):
    data = request.get_json()
    answer = data.get('answer')

    review = professor_controller.submit_answer(answer, review_id)

    if review:
        return jsonify(review.serialize())
    else:
        return jsonify({'error': 'Review not found'}), 404
