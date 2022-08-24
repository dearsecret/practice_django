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
