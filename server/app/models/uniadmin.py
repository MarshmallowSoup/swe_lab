from database import db

class UniversityAdmin(db.Model):
    __tablename__ = 'uniadmin'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    university = db.Column(db.String(100), nullable=False)
    
    reviews = db.relationship('UniversityReview', backref='uniadmin', lazy=True)

    def __repr__(self):
        return f"UniversityAdmin('{self.username}', '{self.email}', '{self.university}')"


    def get_id(self):
        return str(self.id)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'university': self.university,
            'student_rating': self.student_rating,
            'university_rating': self.university_rating
        }