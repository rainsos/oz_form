from flask import Blueprint, request, jsonify
from app.services import users, questions, choices, images, answers

# Blueprint 생성 - 라우트 모음
routes = Blueprint("routes", __name__)

# 1. 기본 연결 확인 API
@routes.route("/", methods=["GET"])
def connect():
    return jsonify({"message": "Success Connect"}), 200

# 2. 메인 이미지 가져오기
@routes.route("/image/main", methods=["GET"])
def get_main_image():
    image_list = images.get_all_images()
    main_image = next((img for img in image_list if img["type"] == "main"), None)
    if main_image:
        return jsonify({"image": main_image["url"]}), 200
    return jsonify({"message": "No main image found"}), 404

# 3.1 회원가입
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

# 3.2 전체 유저 목록 조회
@routes.route("/users", methods=["GET"])
def get_users():
    return jsonify(users.get_all_users()), 200
  
# 4.1 특정 질문 + 선택지 조회
@routes.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    question = questions.get_question_by_id(question_id)   # 직접 조회!
    if not question:
        return jsonify({"message": "Question not found"}), 404

    choices_list = choices.get_choices_by_question(question_id)
    question["choices"] = choices_list
    return jsonify(question), 200

# 4.2 질문 개수 반환
@routes.route("/questions/count", methods=["GET"])
def question_count():
    total = len(questions.get_all_questions())
    return jsonify({"total": total}), 200

# 4.2 전체 질문 목록 조회
@routes.route("/questions/all", methods=["GET"])
def get_all_questions():
    all_questions = questions.get_all_questions()
    return jsonify(all_questions), 200  

# 5. 특정 질문의 선택지 리스트 조회
@routes.route("/choice/<int:question_id>", methods=["GET"])
def get_choice_list(question_id):
    choice_list = choices.get_choices_by_question(question_id)
    return jsonify({"choices": choice_list}), 200

# 6. 답변 제출 API
@routes.route("/submit", methods=["POST"])
def submit_answers():
    data = request.json
    for ans in data:
        answers.save_answer(user_id=ans["user_id"], choice_id=ans["choice_id"])
    return jsonify({"message": f"User: {data[0]['user_id']}'s answers Success Create"}), 200

# 7.1 이미지 생성 API
@routes.route("/image", methods=["POST"])
def create_image():
    data = request.json
    image = images.create_image(url=data["url"], image_type=data["type"])
    return jsonify({"message": f"ID: {image['id']} Image Success Create"}), 201

# 7.2 질문 생성 API
@routes.route("/question", methods=["POST"])
def create_question():
    data = request.json
    question = questions.create_question(
        title=data["title"], sqe=data["sqe"], image_id=data["image_id"]
    )
    return jsonify({"message": f"Title: {question['title']} question Success Create"}), 201

# 7.3 선택지 생성 API
@routes.route("/choice", methods=["POST"])
def create_choice():
    data = request.json
    choice = choices.create_choice(
        content=data["content"], sqe=data["sqe"], question_id=data["question_id"]
    )
    return jsonify({"message": f"Content: {choice['content']} choice Success Create"}), 201
  