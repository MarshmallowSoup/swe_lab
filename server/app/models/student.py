from database import db
from email_validator import validate_email, EmailNotValidError

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    # Relationships
    reviews = db.relationship('Review', backref='student', lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.validate_email(email)
        self.email = email
        self.password = password

    def __repr__(self):
        return f"Student('{self.first_name} {self.last_name}', '{self.email}')"

    def validate_email(self, email):
        try:
            v = validate_email(email)
            email = v["email"]
            if "lpnu.ua" not in email:
                raise EmailNotValidError("Email domain must be @lpnu.ua")
        except EmailNotValidError as e:
            raise ValueError(str(e))


    def get_id(self):
        return str(self.id)
    
    @property
    def is_active(self):
        # For simplicity, always return True. You might implement more
        # sophisticated logic here based on your application's requirements.
        return True
    

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
