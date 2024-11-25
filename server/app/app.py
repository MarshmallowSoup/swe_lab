from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from routes import auth_blueprint,student_blueprint, university_admin_blueprint, sysadmin_blueprint
from controllers import Analytics, AuthController, ProfessorController, StudentController, SysAdminController, UniversityAdminController
from database import db
from models import UniversityAdmin, UniversityReview, Professor, SystemAdmin, Review, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@127.0.0.1:5432/prof_rating'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(student_blueprint, url_prefix='/student')
app.register_blueprint(university_admin_blueprint, url_prefix='/uniadmin')
app.register_blueprint(sysadmin_blueprint, url_prefix='/sysadmin')


# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Initialize AuthController with the Flask app instance
auth_controller = AuthController(app)
app.config['auth_controller'] = auth_controller
# Initialize SQLAlchemy
db.init_app(app)

# Add your models to the database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
