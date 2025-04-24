from app.models import Answer
from config import db

def save_answer(user_id, choice_id):
    answer = Answer(user_id=user_id, choice_id=choice_id)
    db.session.add(answer)
    db.session.commit()
    return answer.to_dict()
