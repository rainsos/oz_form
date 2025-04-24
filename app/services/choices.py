from app.models import Choices
from config import db

def create_choice(content, sqe, question_id):
    choice = Choices(content=content, sqe=sqe, question_id=question_id)
    db.session.add(choice)
    db.session.commit()
    return choice.to_dict()

def get_choices_by_question(question_id):
    choices_list = Choices.query.filter_by(question_id=question_id).all()
    return [c.to_dict() for c in choices_list]

def update_choice_content(choice_id, new_content):
    choice = Choices.query.get(choice_id)
    if choice:
        choice.content = new_content
        db.session.commit()
        return choice.to_dict()
    return None

def delete_choice(choice_id):
    choice = Choices.query.get(choice_id)
    if choice:
        db.session.delete(choice)
        db.session.commit()
        return True
    return False


def delete_choice(choice_id):
    choice = Choices.query.get(choice_id)
    if choice:
        db.session.delete(choice)
        db.session.commit()
        return True
    return False
