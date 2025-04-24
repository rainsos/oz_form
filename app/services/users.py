from app.models import User
from config import db

# 사용자 생성 함수
def create_user(name, age, gender, email):
    user = User(name=name, age=age, gender=gender, email=email)
    db.session.add(user)
    db.session.commit()
    return user.to_dict()

# 모든 사용자 조회 함수
def get_all_users():
    users = User.query.all()
    return [user.to_dict() for user in users]

# 사용자 이메일 수정 함수
def update_user_email(user_id, new_email):
    user = User.query.get(user_id)
    if user:
        user.email = new_email
        db.session.commit()
        return user.to_dict()
    return None

# 사용자 삭제 함수
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

