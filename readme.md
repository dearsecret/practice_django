# 1. 세팅

1. Linter 검색 후 추가
   Select InterPreter 추가
   수동 설치 :
   settings.json >
   "python.formatting.provider": "black",
   "python.linting.flake8Args": ["--max-line-length=88"]

2. .gitignore >
   python .gitignore 추가
   DS_Store 추가

3. django-admin startproject config
   외부파일로 디렉터리 변경

4. django-admin startapp 정의
   users / rooms / reservations / conversations / lists
   공통항목으로 core

# 2. User

DJANGO REF - Auth user

1. config > settings.py > auth_user_model 설정 / app설치

2. User model 및 admin 작성 (auth 해당)

3. 저장시 black 설치 요구

4. Pillow 설치 요구

5. python manage.py
   createsuperuser 작성
   makemigrations / migrate / runserver

- login issue db.sqlite3 삭제하고 createsuperuser 진행하면 해결됨.

# 3. Core

    TimeStampModel 생성 및 설정

# 4. rooms

    Third Party : django-countries 설치
    models 정의 /
    ForeignKey / ManytoManyField /
    __str__ class

    meta / abstract
    verbose_name vs verbose_name_plural
