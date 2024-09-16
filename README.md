# meogibogo
먹이보고 푸드 커뮤니티
# MyProject (먹이보고)

## 프로젝트 설명
먹이보고는 사용자가 음식 리뷰를 커뮤니티에 공유할 수 있는 Django 기반의 웹 애플리케이션입니다.

## 환경 설정

이 프로젝트는 `pyenv`와 `Poetry`를 사용하여 Python 환경을 관리합니다.

### 1. 요구사항
- `pyenv` (Python 버전 관리)
- `Poetry` (패키지 관리 및 의존성 관리)
- Python 3.11.x

### 2. pyenv 설치 및 Python 버전 설정

```bash
# pyenv 설치
curl https://pyenv.run | bash
# 설치 후 아래 명령어로 환경 변수 설정
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

# 프로젝트에 사용할 Python 버전 설치 및 설정
pyenv install 3.11.4
pyenv local 3.11.4
```

### 3. 프로젝트 구조
```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── food/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── templates/
│       └── food/
│           └── index.html
└── static/
    ├── images/
    │   └── example.jpg
    ├── css/
    │   └── styles.css
    └── js/
        └── scripts.js
```

- manage.py: Django 프로젝트를 관리하는 커맨드라인 유틸리티입니다. 서버를 실행하거나, 데이터베이스 마이그레이션을 수행하는 등 다양한 작업을 수행할 수 있습니다.

- myproject/: 프로젝트의 설정과 관련된 파일들이 들어있는 폴더입니다.

- __init__.py: 이 폴더가 파이썬 패키지로 인식되도록 합니다.
- asgi.py: ASGI (Asynchronous Server Gateway Interface) 서버에 대한 설정 파일입니다.
- settings.py: 프로젝트의 설정 파일로, 데이터베이스 설정, 앱 등록, 미들웨어 설정 등을 포함합니다.
- urls.py: URL 라우팅을 설정하는 파일입니다. 요청된 URL과 이를 처리할 뷰 함수를 연결합니다.
- wsgi.py: WSGI (Web Server Gateway Interface) 서버에 대한 설정 파일입니다. 주로 배포 환경에서 사용됩니다.

food/: 생성한 앱의 폴더입니다. 여기에는 앱의 로직이 들어가며, 기본적인 파일들은 다음과 같습니다.

- __init__.py: 이 폴더가 파이썬 패키지로 인식되도록 합니다.
- admin.py: Django 관리자 페이지에서 사용할 모델을 등록하는 파일입니다.
- apps.py: 앱에 대한 설정 파일입니다.
- models.py: 데이터베이스 테이블을 정의하는 파일입니다.
- tests.py: 앱의 테스트 케이스를 정의하는 파일입니다.
- views.py: 요청을 처리하고 응답을 반환하는 함수나 클래스를 정의하는 파일입니다.
- migrations/: 데이터베이스 스키마의 변화를 기록하는 마이그레이션 파일들이 저장되는 폴더입니다.