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
    pip install django-phonenumber-field
    pip install phonenumbers

## API 정리
### 회원가입/로그인/로그아웃
### 회원가입
### 127.0.0.1:8000/auth/registration/ - POST
    {
        "email":"이메일주소",
        "password1":"비밀번호",
        "password2":"비밀번호 확인",
        "name":"이름"
    }
### 로그인
### 127.0.0.1:8000/auth/login/ - POST
    {
        "email":"이메일주소",
        "password":"비밀번호"
    }
### 로그아웃
### 127.0.0.1:8000/auth/logout - POST
    값 필요 X


### ProfileImage
### 프로필 사진 등록하기
### 127.0.0.1:8000/mypage/ - POST
    {
        "profileimage" : 사진 첨부하면 됨
    }
### 프로필 사진 불러오기, 수정하기, 삭제하기
### 불러오기
### 127.0.0.1:8000/mypage/<int:id>/ - GET
#### 결과
    {
        "id" : "해당 사진 id값",
        "profileimage" : "해당 사진"
    }
### 수정하기
### 127.0.0.1:8000/mypage/<int:id>/ - PUT(PATCH)
    {
        "profileimage" : 사진 첨부하면 됨
    }
### 삭제하기
### 127.0.0.1:8000/mypage/<int:id>/ - DELETE
#### 결과
    아무것도 안 뜸
