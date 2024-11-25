from models import Student, Review, Professor, UniversityReview
from database import db
from sqlalchemy import func

class Analytics:

    def get_comments(self, professor_id):
        # Retrieve comments from reviews by professor id
        reviews = Review.query.filter_by(professor_id=professor_id).all()

        comments_data = []

        for review in reviews:
            student = Student.query.get(review.student_id)

            student_name = "Anonymous" if review.anonymous else student.first_name
            comment_data = {
                "student_name": student_name,
                "rate" : review.rating,
                "comment": review.comment
            }

            comments_data.append(comment_data)

        return comments_data
    

    def calculate_average_university_rating(self, professor_id):
        # Calculate average university rating based on professor's university reviews
        average_professor_rating = db.session.query(func.avg(UniversityReview.professor_rating)).filter_by(professor_id=professor_id).scalar() or 0.0
        average_course_rating = db.session.query(func.avg(UniversityReview.course_rating)).filter_by(professor_id=professor_id).scalar() or 0.0

        # Calculate the overall average as the mean of professor_rating and course_rating
        average_university_rating = (average_professor_rating + average_course_rating) / 2.0

        return average_university_rating

    def update_university_rating(self, professor_id):
        # Calculate average university rating
        average_university_rating = self.calculate_average_university_rating(professor_id)

        # Update professor's university_rating field
        professor = Professor.query.get(professor_id)
        if professor:
            professor.university_rating = average_university_rating

            # Commit the changes to the database
            db.session.commit()
        else:
            print("Professor not found.")

    def calculate_average_students_rating(self, professor_id):
        # Calculate average rating based on reviews
        average_rating = Review.query.with_entities(func.avg(Review.rating)).filter_by(professor_id=professor_id).scalar() or 0.0

        return average_rating
    

    def update_student_rating(self, professor_id):
        # Calculate average rating based on reviews
        average_rating = self.calculate_average_students_rating(professor_id)

        # Update professor's student_rating field
        professor = Professor.query.get(professor_id)
        if professor:
            professor.student_rating = average_rating

            # Commit the changes to the database
            db.session.commit()
        else:
            print("Professor not found.")
