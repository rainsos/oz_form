#  개발 환경에서 Flask 애플리케이션을 실행하는 파일

from app import create_app

# Flask 애플리케이션 인스턴스 생성
application = create_app()

# 개발 환경에서 직접 실행할 때 진입점
if __name__ == "__main__":
    application.run(debug=True)