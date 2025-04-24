from app.models import Question
from config import db

def create_question(title, sqe, image_id):
    question = Question(title=title, sqe=sqe, image_id=image_id)
    db.session.add(question)
    db.session.commit()
    return question.to_dict()

def get_all_questions():
    questions = Question.query.all()
    return [q.to_dict() for q in questions]

def update_question_title(question_id, new_title):
    question = Question.query.get(question_id)
    if question:
        question.title = new_title
        db.session.commit()
        return question.to_dict()
    return None

def delete_question(question_id):
    question = Question.query.get(question_id)
    if question:
        db.session.delete(question)
        db.session.commit()
        return True
    return False

