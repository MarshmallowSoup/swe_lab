from database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.Text)
    anonymous = db.Column(db.Boolean, default=False)
    answer = db.Column(db.Text)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)

    def __repr__(self):
        return f"Review('{self.rating}', '{self.comment[:20]}', '{self.anonymous}')"
    
    def get_id(self):
        return str(self.id)