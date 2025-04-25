#!/bin/bash

set -e  # 오류 발생 시 즉시 종료

# 오류 발생 시 오류 메시지를 출력하는 함수
trap 'echo "Error occurred in script at line $LINENO"; exit 1' ERR

echo "==== Check Virtual environment ===="
echo

# 스크립트가 실행된 디렉토리에서 루트 디렉토리 추정
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_DIR=$(dirname "$SCRIPT_DIR")  # scripts 상위 디렉토리를 루트 디렉토리로 간주
VENV_DIR="$REPO_DIR/.venv"

cd ..

# 현재 가상환경 확인 및 활성화
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Virtual environment is not active. Activating .venv..."

    # .venv 활성화
    if [ -f "$VENV_DIR/bin/activate" ]; then
        source "$VENV_DIR/bin/activate"
    else
        echo "Virtual environment not found at '$VENV_DIR'. Please ensure it exists."
        exit 1
    fi
else
    echo "Virtual environment is already active: $VIRTUAL_ENV"
fi

echo "==== Starting Migration ===="
echo

# 🔥 이 두 줄 추가!
export FLASK_APP=run
export FLASK_ENV=development

# Flask 마이그레이션 작업
flask db init
flask db migrate
flask db upgrade

echo "==== Migration Completed ===="
