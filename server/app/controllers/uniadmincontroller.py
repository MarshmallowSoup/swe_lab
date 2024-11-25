from database import db
from models import UniversityAdmin, UniversityReview 


class UniversityAdminController:

    @staticmethod
    def create_university_admin(first_name, last_name, username, email, password, university):
        # Create a new university admin
        new_admin = UniversityAdmin(first_name=first_name, last_name=last_name, username=username, email=email, password=password, university=university)

        # Add the new admin to the database session
        db.session.add(new_admin)

        # Commit the changes to the database
        db.session.commit()

        # Return the created admin object
        return new_admin

    def get_admin_by_username(self, username):
        # Retrieve an admin by username
        admin = UniversityAdmin.query.filter_by(username=username).first()
        return admin

    @staticmethod
    def validate_login_credentials(username, password):
        # Validate login credentials and return the admin if valid
        admin = UniversityAdmin.query.filter_by(username=username, password=password).first()
        return admin

    def create_university_review(self, admin_id, professor_rating, course_rating, professor_id):
        # Create a new university review
        admin = UniversityAdmin.query.get(admin_id)
        if admin:
            new_review = UniversityReview(professor_rating=professor_rating, course_rating=course_rating, professor_id=professor_id, author_id=admin)
            db.session.add(new_review)
            db.session.commit()
            return new_review
        else:
            return None


    def list_all_university_admins(self):
        # List all university admins
        university_admins = UniversityAdmin.query.all()
        return university_admins

    # Function to get a university admin by ID
    def get_university_admin_by_id(self, admin_id):
        return UniversityAdmin.query.get(admin_id)