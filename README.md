# Univment_back
## 동국대학교 멋쟁이사자처럼 2학기 프로젝트 Univment
## 실행

### 라이브러리 설치
    pip install django
    pip install pillow
    pip install dj-rest-auth
    pip install django-allauth
    pip install djangorestframework
    pip install djangorestframework-simplejwt

## API 정리
### 회원가입/로그인/로그아웃
### 회원가입
### 127.0.0.1:8000/auth/registration/ - POST
    {
        "username":"사용자이름",
        "email":"이메일주소",
        "password1":"비밀번호",
        "password2":"비밀번호 확인"
    }
### 로그인
### 127.0.0.1:8000/auth/login/ - POST
    {
        "username":"사용자이름(필수X)",
        "email":"이메일주소",
        "password":"비밀번호"
    }
### 로그아웃
### 127.0.0.1:8000/auth/logout - POST
    값 필요 X
