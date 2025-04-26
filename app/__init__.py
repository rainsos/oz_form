from flask_smorest import Api
from app.routes import routes
from config import db
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS

import app.models

migrate = Migrate()

def create_app():
    application = Flask(__name__)

    # 기본 설정
    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    # Swagger 관련 설정
    application.config["API_TITLE"] = "OZ 설문조사 API 문서"
    application.config["API_VERSION"] = "v1"
    application.config["OPENAPI_VERSION"] = "3.0.2"
    application.config["OPENAPI_URL_PREFIX"] = "/"
    application.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    application.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    db.init_app(application)
    migrate.init_app(application, db)

    # CORS 설정 추가
    CORS(application, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    # 400 에러 핸들링
    @application.errorhandler(400)
    def handle_bad_request(error):
        response = jsonify({"message": error.description})
        response.status_code = 400
        return response

    # Api 객체 생성 (title 없이)
    api = Api(application)

    # Blueprint 등록
    api.register_blueprint(routes)

    return application

