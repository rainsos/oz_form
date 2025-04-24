from app.models import Question
from config import db

# 질문 생성 함수
def create_question(title, sqe, image_id):
    question = Question(title=title, sqe=sqe, image_id=image_id)
    db.session.add(question)
    db.session.commit()
    return question.to_dict()

# 모든 질문 조회 함수
def get_all_questions():
    questions = Question.query.all()
    return [q.to_dict() for q in questions]

# 특정 질문 ID로 조회 함수  
def get_question_by_id(question_id):
    question = Question.query.get(question_id)
    if question:
        return question.to_dict()
    return None

# 질문 제목 수정 함수
def update_question_title(question_id, new_title):
    question = Question.query.get(question_id)
    if question:
        question.title = new_title
        db.session.commit()
        return question.to_dict()
    return None

# 질문 삭제 함수
def delete_question(question_id):
    question = Question.query.get(question_id)
    if question:
        db.session.delete(question)
        db.session.commit()
        return True
    return False

