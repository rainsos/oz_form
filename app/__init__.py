from flask_smorest import Api
from app.routes import routes
from config import db
from flask import Flask, jsonify
from flask_migrate import Migrate

import app.models


migrate = Migrate()


def create_app():
    application = Flask(__name__)

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)

    migrate.init_app(application, db)

		# 400 에러 발생 시, JSON 형태로 응답 반환
    @application.errorhandler(400)
    def handle_bad_request(error):
        response = jsonify({"message": error.description})
        response.status_code = 400
        return response

		# 블루프린트 등록 및 Swagger-UI 연동
    api = Api(application)   # 🔹 Api 객체 생성
    api.register_blueprint(routes)  # 🔹 기존 Blueprint 등록


    return application
