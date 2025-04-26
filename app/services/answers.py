from app.models import Answer, Choices
from config import db
from sqlalchemy import func

# 사용자 답변 저장 함수
def save_answer(user_id, choice_id):
    answer = Answer(user_id=user_id, choice_id=choice_id)
    db.session.add(answer)
    db.session.commit()
    return answer.to_dict()

# ✅ 선택지별 전체 응답 수와 비율 구하는 함수
def get_answer_rate_by_choice():
    total_answers = db.session.query(func.count(Answer.id)).scalar()

    if total_answers == 0:
        return []

    results = (
        db.session.query(
            Answer.choice_id,
            func.count(Answer.id).label('answer_count')
        )
        .group_by(Answer.choice_id)
        .all()
    )

    return [
        {
            "choice_id": choice_id,
            "answer_count": count,
            "percentage": round((count / total_answers) * 100, 2)
        }
        for choice_id, count in results
    ]

# ✅ 질문별 응답 수 구하는 함수
def get_answer_count_grouped_by_question():
    results = (
        db.session.query(
            Choices.question_id,  # ✅ 수정
            func.count(Answer.id).label('answer_count')
        )
        .join(Choices, Choices.id == Answer.choice_id)  # ✅ 수정
        .group_by(Choices.question_id)
        .all()
    )

    return [
        {
            "choice_id": question_id,
            "answer_count": count,
            "percentage": None
        }
        for question_id, count in results
    ]
