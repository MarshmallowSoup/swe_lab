from database import db
from models import Professor, Review

class ProfessorController:
    def get_professor_by_id(self, professor_id):
        # Retrieve a professor by ID
        professor = Professor.query.get(professor_id)
        return professor

    def get_professor_reviews(self, professor_id):
        # Retrieve reviews for a professor
        reviews = Review.query.filter_by(professor_id=professor_id).all()
        return reviews


    def list_all_professors(self):
        # List all professors
        professors = Professor.query.all()
        return professors
    
    @staticmethod
    def create_professor(name, email, password, subject, university):
        # Create a new professor
        new_professor = Professor(name=name, email=email, password=password, subject=subject, university=university)

        # Add the new professor to the database session
        db.session.add(new_professor)

        # Commit the changes to the database
        db.session.commit()

        # Return the created professor object
        return new_professor

    def update_professor_info(self, professor_id, new_info):
        # Update professor information
        professor = Professor.query.get(professor_id)
        if professor:
            for key, value in new_info.items():
                setattr(professor, key, value)
            db.session.commit()
            return professor
        else:
            return None

    def validate_login_credentials(self, email, password):
        # Validate login credentials and return the professor if valid
        professor = Professor.query.filter_by(email=email, password=password).first()
        return professor
    
    def submit_answer(self, answer, review_id):
        # Submit an answer for a professor
        review = Review.query.get(review_id)
        review.answer = answer
        db.session.commit()
        return review