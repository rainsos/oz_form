from flask_smorest import Blueprint
from flask import request, jsonify, render_template, current_app as app
from app.services import users, questions, choices, images, answers
from app.models import Question
from config import db
from flask_cors import cross_origin

routes = Blueprint("routes", __name__)

# 1. 기본 연결 확인
@routes.route("/", methods=["GET"])
@cross_origin(origins="https://oz-flask-form.vercel.app", supports_credentials=True)
def connect():
    return jsonify({"message": "Success Connect"}), 200

# 2. 회원가입 및 유저 관리
@routes.route("/signup", methods=["POST"])
def signup():
    data = request.json
    try:
        user = users.create_user(
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            email=data["email"]
        )
        return jsonify({
            "message": f"{user['name']}님 회원가입을 축하합니다",
            "user_id": user["id"]
        }), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@routes.route("/users", methods=["GET"])
def get_users():
    return jsonify(users.get_all_users()), 200

# 3. 이미지 관리
@routes.route("/image", methods=["POST"])
def create_image():
    data = request.json
    image = images.create_image(url=data["url"], image_type=data["type"])
    return jsonify({"message": f"ID: {image['id']} Image Success Create"}), 201

@routes.route("/image/main", methods=["GET"])
def get_main_image():
    image_list = images.get_all_images()
    main_image = next((img for img in image_list if img["type"] == "main"), None)
    if main_image:
        return jsonify({"image": main_image["url"]}), 200
    return jsonify({"message": "No main image found"}), 404

# 4. 질문 및 선택지 관리
@routes.route("/question", methods=["POST"])
def create_question():
    data = request.json
    question = questions.create_question(
        title=data["title"], sqe=data["sqe"], image_id=data["image_id"]
    )
    return jsonify({"message": f"Title: {question['title']} question Success Create"}), 201

@routes.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    question = questions.get_question_by_id(question_id)
    if not question:
        return jsonify({"message": "Question not found"}), 404

    if question.get("image"):
        question["image"] = question["image"]["url"]

    choices_list = choices.get_choices_by_question(question_id)
    question["choices"] = choices_list
    return jsonify(question), 200

@routes.route("/questions/all", methods=["GET"])
def get_all_questions():
    all_questions = questions.get_all_questions()
    return jsonify(all_questions), 200

@routes.route("/questions/count", methods=["GET"])
def question_count():
    total = len(questions.get_all_questions())
    return jsonify({"total": total}), 200

@routes.route("/choice", methods=["POST"])
def create_choice():
    data = request.json
    choice = choices.create_choice(
        content=data["content"], sqe=data["sqe"], question_id=data["question_id"]
    )
    return jsonify({"message": f"Content: {choice['content']} choice Success Create"}), 201

@routes.route("/choice/<int:question_id>", methods=["GET"])
def get_choice_list(question_id):
    choice_list = choices.get_choices_by_question(question_id)
    return jsonify({"choices": choice_list}), 200

# 5. 답변 제출
@routes.route("/submit", methods=["POST"])
def submit_answers():
    data = request.json
    for ans in data:
        answers.save_answer(user_id=ans["user_id"], choice_id=ans["choice_id"])
    return jsonify({"message": f"User: {data[0]['user_id']}'s answers Success Create"}), 200

# 6. 통계 API
@routes.route("/stats/answer_rate_by_choice", methods=["GET"])
def get_answer_rate_by_choice():
    results = answers.get_answer_rate_by_choice()
    return jsonify(results), 200

@routes.route("/stats/answer_count_by_question", methods=["GET"])
def get_answer_count_by_question():
    results = answers.get_answer_count_grouped_by_question()
    return jsonify(results), 200

# 7. 기타 개발용 (index.html 직접 보기)
@routes.route("/client", methods=["GET"])
def frontend():
    return render_template('index.html')

# 8. 질문 이미지 ID 수정용 (임시)
@routes.route("/question/<int:question_id>/update_image", methods=["PUT"])
def update_question_image(question_id):
    data = request.json
    new_image_id = data["image_id"]
    question = Question.query.get(question_id)
    if question:
        question.image_id = new_image_id
        db.session.commit()
        return jsonify({"message": f"Question {question_id} image updated to {new_image_id}"}), 200
    return jsonify({"message": "Question not found"}), 404
