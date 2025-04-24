# wsgi.py = Flask 앱을 외부 서버 연결해주는 역할
# 초기 migrate 작업시 오류 잡기위해 설정(배포용 기본셋팅)

from app import create_app

application = create_app()