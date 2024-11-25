from flask_login import LoginManager, login_user, logout_user, current_user
from .studentcontroller import StudentController
from .professorcontroller import ProfessorController
from .uniadmincontroller import UniversityAdminController
from .sysadmincontroller import SysAdminController
from models  import Student, Professor, UniversityAdmin, SystemAdmin

class AuthController:
    def __init__(self, app):
        self.login_manager = LoginManager()
        self.login_manager.init_app(app)
        

    def login(self, user_type, email, password):
        # Login user based on user type
        user = None

        if user_type == 'student':
            user = StudentController.validate_login_credentials(email, password)
        elif user_type == 'professor':
            user = ProfessorController.validate_login_credentials(email, password)
        elif user_type == 'university_admin':
            user = UniversityAdminController.validate_login_credentials(email, password)
        elif user_type == 'system_admin':
            user = SysAdminController.validate_login_credentials(email, password)

        if user and user.password == password:
            login_user(user)
            return True
        else:
            return False


    def register(self, user_type, email, password, **kwargs):
        # Register user based on user type

        if user_type == 'student':
            first_name = kwargs.get('first_name', None)
            last_name = kwargs.get('last_name', None)
            student = StudentController
            student.create_student(first_name=first_name,last_name=last_name , email=email, password=password)
        elif user_type == 'professor':
            name = kwargs.get('name', None)
            subject = kwargs.get('subject', None)
            university = kwargs.get('university', None)
            ProfessorController.create_professor(name=name, email=email, password=password, subject=subject, university=university)
        elif user_type == 'university_admin':
            first_name = kwargs.get('first_name', None)
            last_name = kwargs.get('last_name', None)
            username = kwargs.get('username', None)
            university = kwargs.get('university', None)
            UniversityAdminController.create_university_admin(first_name=first_name, last_name=last_name, username=username, email=email, password=password, university=university)
        elif user_type == 'system_admin':
            username = kwargs.get('username', None)
            SysAdminController.create_sysadmin(username=username, email=email, password=password)

        return True
    

    def logout(self):
        logout_user()

    def get_current_user(self):
        return current_user