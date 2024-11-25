from database import db
from models  import Student, Professor, UniversityAdmin, Review, SystemAdmin

class SysAdminController:

    def delete_user(self, user_id, user_type):
        # Delete a user by ID based on user type
        user = None

        if user_type == 'student':
            user = Student.query.get(user_id)
        elif user_type == 'professor':
            user = Professor.query.get(user_id)
        elif user_type == 'university_admin':
            user = UniversityAdmin.query.get(user_id)

        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        else:
            return False

    def validate_login_credentials(self, email, password):
        # Validate login credentials and return the admin if valid
        admin = SystemAdmin.query.filter_by(email=email, password=password).first()
        return admin

    def delete_inappropriate_review(self, review_id):
        # Delete an inappropriate review by ID
        review = Review.query.get(review_id)
        
        if review:
            db.session.delete(review)
            db.session.commit()
            return True
        else:
            return False
        
    
    def create_student(self, first_name, last_name, email, password):
        # Create a new student
        new_student = Student(first_name=first_name, last_name=last_name, email=email, password=password)

        # Add the new student to the database session
        db.session.add(new_student)

        # Commit the changes to the database
        db.session.commit()

        # Return the created student object
        return new_student

    def create_professor(self, name, email, subject, university, password):
        # Create a new professor
        new_professor = Professor(name=name, email=email, subject=subject, university=university, password=password)

        # Add the new professor to the database session
        db.session.add(new_professor)

        # Commit the changes to the database
        db.session.commit()

        # Return the created professor object
        return new_professor

    def create_university_admin(self, username, email, password, university):
        # Create a new university admin
        new_admin = UniversityAdmin(username=username, email=email, password=password, university=university)

        # Add the new admin to the database session
        db.session.add(new_admin)

        # Commit the changes to the database
        db.session.commit()

        # Return the created admin object
        return new_admin
    
    @staticmethod
    def create_sysadmin(username, email, password):
        # Create a new system admin
        new_sysadmin = SystemAdmin(username=username, email=email, password=password)

        # Add the new sysadmin to the database session
        db.session.add(new_sysadmin)

        # Commit the changes to the database
        db.session.commit()

        # Return the created sysadmin object
        return new_sysadmin

    # Update function
    def update_sysadmin_info(self, sysadmin_id, new_info):
        # Update system admin information
        sysadmin = SystemAdmin.query.get(sysadmin_id)
        if sysadmin:
            for key, value in new_info.items():
                setattr(sysadmin, key, value)
            db.session.commit()
            return sysadmin
        else:
            return None
        
    def list_all_students(self):
        # List all students
        students = Student.query.all()
        return students

    def list_all_professors(self):
        # List all professors
        professors = Professor.query.all()
        return professors

    def list_all_university_admins(self):
        # List all university admins
        university_admins = UniversityAdmin.query.all()
        return university_admins

    def list_all_system_admins(self):
        # List all system admins
        system_admins = SystemAdmin.query.all()
        return system_admins    

    # Function to get a student by ID
    def get_student_by_id(self, student_id):
        return Student.query.get(student_id)

    # Function to get a professor by ID
    def get_professor_by_id(self, professor_id):
        return Professor.query.get(professor_id)

    # Function to get a university admin by ID
    def get_university_admin_by_id(self, admin_id):
        return UniversityAdmin.query.get(admin_id)

    # Function to get a system admin by ID
    def get_system_admin_by_id(self, sysadmin_id):
        return SystemAdmin.query.get(sysadmin_id)