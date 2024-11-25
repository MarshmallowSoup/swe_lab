from database import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    university = db.Column(db.String(100), nullable=False)
    student_rating = db.Column(db.Float, default=0.0)
    university_rating = db.Column(db.Float, default=0.0)
    
    # Relationships
    reviews = db.relationship('Review', backref='professor', lazy=True)

    def __repr__(self):
        return f"Professor('{self.name}', '{self.subject}', '{self.university}')"

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