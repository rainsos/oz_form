# 📌 Flask 심리테스트 웹 애플리케이션

## 👥 Team Members

### 🎨 Backend

<table align="center">
  <tr>
    <th style="text-align: center;">이소영</th>
    <th style="text-align: center;">이정호</th>
    <th style="text-align: center;">이상인</th>
  </tr>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/201067243?v=4" width="100"/></td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/201067201?v=4" width="100"/></td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/201066934?v=4" width="100"/></td>
  </tr>
  <tr>
    <td align="center">@soyoung1105</td>
    <td align="center">@leemera</td>
    <td align="center">@rainsos</td>
  </tr>
</table>
                          


## 🚀 개요

이 프로젝트는 **Flask** 기반으로 제작된 웹 애플리케이션으로, 사용자의 성향과 특성을 분석하는 **설문조사 및 심리테스트**를 제공합니다.  
간편한 회원가입을 통해 사용자는 설문에 참여하고 **개인화된 결과**를 즉시 확인할 수 있습니다.  

> 본 프로젝트는 팀 프로젝트로 기획되었으며  
> `Flask`, `Flask-Smorest`, `Flask-SQLAlchemy`, `MySQL`, `Postman`, `GitHub`, `AWS EC2`를 활용하여 개발 및 배포하였습니다.



## 📌 프로젝트 구조

```plaintext
oz_form/                        # 프로젝트 폴더
├── .venv/                      # 가상환경   
├── app/                        # Flask 애플리케이션 코드 폴더
│   ├── __init__.py             # 앱 초기화 및 설정 파일
│   ├── services/               # DB 상호작용 orm 코드 폴더
│   │   ├── users.py            # users 테이블 관련 orm 함수
│   │   ├── questions.py        # questions 테이블 관련 orm 함수
│   │   ├── choices.py          # choices 테이블 관련 orm 함수
│   │   ├── images.py           # images 테이블 관련 orm 함수
│   │   └── answers.py          # answers 테이블 관련 orm 함수
│   ├── models.py               # SQLAlchemy 모델 정의
│   ├── routes.py               # 뷰 및 라우트 정의
├── config.py                   # Flask 및 데이터베이스 설정 파일
├── requirements.txt            # 필요한 Python 패키지 목록
├── run.py                      # 개발환경에서 테스트 하는 실행 파일
├── wsgi.py                     # 배포환경에서의 실행 파일
└── migrations/                 # Flask-Migrate를 위한 DB 마이그레이션 파일
```

## 🛠 주요 기능

- ✅ **회원가입 및 로그인**: 간편한 사용자 인증을 제공합니다.
- ✅ **메인 화면**: 테스트 시작 전 대표 이미지를 제공하여 흥미를 유발합니다.
- ✅ **설문 진행**: 순차적으로 제공되는 객관식 질문을 통해 사용자의 응답을 수집합니다.
- ✅ **답변 제출 및 결과 확인**: 모든 질문 응답 후, 사용자는 즉시 심리테스트 결과를 확인할 수 있습니다.
- ✅ **관리자 페이지**: 질문과 선택지를 관리하고 업데이트할 수 있습니다.


## 📖 사용 방법

1. **회원가입**  
   메인 화면에서 이름, 이메일, 연령대, 성별을 입력하여 회원가입합니다.

2. **테스트 진행**  
   로그인 후 메인 화면에서 "테스트 시작" 버튼을 클릭하여 설문을 시작합니다.

3. **응답 제출**  
   제공되는 질문에 대해 원하는 선택지를 클릭하여 응답을 제출합니다.

4. **결과 확인**  
   모든 질문 응답 후, 자동으로 결과 페이지가 표시됩니다.

> 🔧 `Postman` 및 `Swagger`를 활용하여 API를 손쉽게 테스트하고 결과를 확인할 수 있습니다.



## 🖥 사용 화면

- **메인 페이지**: 사용자 로그인 후 테스트 시작 안내 및 대표 이미지 제공  
- **질문 페이지**: 질문 및 선택지 화면 제공  
- **결과 페이지**: 테스트 완료 후 개인화된 결과 안내  



## ⚠️ 에러 처리

- **회원가입 오류**: 이미 존재하는 이메일로 가입 시 친절한 오류 메시지를 반환합니다.
- **입력 유효성 검사**: 필수 입력값 누락 또는 잘못된 데이터 형식 입력 시 즉시 알림을 제공합니다.
- **API 호출 실패**: 서버 연결 또는 요청 실패 시 사용자 친화적 메시지를 제공합니다.

> 모든 에러 처리는 사용자가 **이해하기 쉬운 형태**로 제공됩니다.



## 📧 문의

기술 지원 및 프로젝트 관련 문의는 아래 이메일로 연락 바랍니다.

📩 **Email**: [rainsos@nate.com](mailto:rainsos@nate.com)

