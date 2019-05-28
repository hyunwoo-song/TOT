```bash
git init
pip install python-decouple

프로젝트 폴더내 .evv 파일 생성
settings.py

from decouple import config

SECRET_KEY = .... 복사후
.env 파일에 붙여넣기
SECRET_KEY=.... (띄어쓰기 없어야함)

settings.py에
SECRET_KEY = config('SECRET_KEY')

app폴더에에 .gitignore파일 생성
.env 추가

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

pip install django-heroku

가장 아래에
# Heroku
import django_heroku
django_heroku.settings(locals())

pip install gunicorn

app폴더내 
Procfile파일 생성
파일내 
web: gunicorn app이름.wsgi

runtime.txt 파일 생성
python-3.6.7

bash에서
pip freeze > requirements.txt

git add .
git commit -m "190516"

heroku login
Email:
Password:

heroku create 이름
git push heroku master

heroku
runconsole 클릭
bash 입력

.env
```

