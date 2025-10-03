# MME Bot API

FastAPI 기반의 MME Bot API 서버 `개발중`

## 🚀 빠른 시작

### 1. Conda 환경 생성 및 활성화

```bash
# Conda 환경 생성
conda env create -f environment.yml

# 환경 활성화
conda activate mme-bot
```

### 2. 환경 변수 설정

```bash
# .env 파일 생성
# secret ...

# 필요에 따라 .env 파일 수정
```

### 3. 서버 실행

```bash
# 개발 모드로 실행
python src/main.py

# 또는 uvicorn 직접 실행
uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
```

### 4. API 문서 확인

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

### docker-compose

```bash
docker compose up -d
```

## 📁 프로젝트 구조

```
# 수정중...
mme-bot/
├── src/
│   ├── config/          # 설정 파일들
│   ├── database/        # 데이터베이스 관련
│   ├── domains/         # 도메인별 모듈
│   │   └── users/       # 사용자 관련
│   └── main.py         # 메인 애플리케이션
├── tests/              # 테스트 파일들
├── requirements.txt    # Python 의존성
├── environment.yml     # Conda 환경 설정
└── README.md          # 프로젝트 문서
```

## 🛠️ 개발 도구

### 코드 포맷팅

```bash
# Black으로 코드 포맷팅
black src/

# isort로 import 정렬
isort src/

# flake8로 코드 검사
flake8 src/
```

### 테스트 실행

```bash
# 모든 테스트 실행
pytest

# 특정 테스트 파일 실행
pytest tests/test_main.py

# 커버리지와 함께 실행
pytest --cov=src
```

## 🔧 설정

주요 설정은 `src/config/settings.py`에서 관리됩니다. 환경 변수를 통해 설정을 오버라이드할 수 있습니다.

### 주요 설정 항목

- `DEBUG`: 디버그 모드 (기본값: True)
- `HOST`: 서버 호스트 (기본값: 127.0.0.1)
- `PORT`: 서버 포트 (기본값: 8000)
- `DATABASE_URL`: 데이터베이스 연결 URL
- `SECRET_KEY`: JWT 토큰용 시크릿 키

## 📦 의존성

주요 의존성:

- **FastAPI**: 웹 프레임워크
- **Uvicorn**: ASGI 서버
- **SQLAlchemy**: ORM
- **Pydantic**: 데이터 검증
- **Python-dotenv**: 환경 변수 관리

전체 의존성 목록은 `requirements.txt`를 참조하세요.

## 🚀 배포

### Docker (선택사항)

```bash
# Docker 이미지 빌드
docker build -t mme-bot-api .

# 컨테이너 실행
docker run -p 8000:8000 mme-bot-api
```

### 프로덕션 실행

```bash
# 프로덕션 모드로 실행
uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📝 API 엔드포인트

- `GET /`: 루트 엔드포인트
- `GET /health`: 헬스 체크
- `GET /docs`: Swagger UI 문서