#  14 workhop

1. 가상환경 생성

```bash
pyenv virtualenv 3.6.7 intro-venv
pyenv local intro-venv

#장고 설치
pip install django

#프로젝트를 시작하겠다
django-admin startproject first_workshop .

# 서버실행 명령어
python manage.py runserver $IP:$PORT
```



2. 오류페이지에서 

   ```
   DisallowedHost at /
   Invalid HTTP_HOST header: 'playground-tot23.c9users.io:8080'. You may need to add 'playground-tot23.c9users.io' to ALLOWED_HOSTS.
   
   playground-tot23.c9users.io를 복사
   ```

   

3. settings.py에서 

   ```python
   ALLOWED_HOSTS = [] 를
   ALLOWED_HOSTS = ['playground-tot23.c9users.io'] 추가
   
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'pages.apps.PagesConfig', <------추가
   ]
   
   
   LANGUAGE_CODE = 'ko-kr' 수정
   
   TIME_ZONE = 'Asia/Seoul' (List of tz data base에서 확인 해서 작성)
   ```

4. bash 창에서 page  생성

   ```bash
   # page 생성
   python manage.py startapp pages
   # page 폴더내 
   templates 폴더 생성
   ```

5. ```python
   # views.py
   def info(request):
       return render(request, 'info.html')
   
   #urls.py
   from pages import views 임포트 해라
   
   urlpatterns = [
       path('info/', views.info),
       path('admin/', admin.site.urls),
   ]
   
   ```

6. page 폴더 내 templates 폴더 생성

   ```
   templates 폴더에
   
   info.html 파일 생성
   ```

7. info.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
   </head>
   <body>
       <h1>우리반정보</h1>
       <h2>teacher</h2>
           <ul>
               <li>
               황준우
               </li>
           </ul>
       <h2>student</h2>
           <ul>
               <li>송현우</li>
               <li>진민지</li>
               <li>JMJ</li>
               <li>권박사</li>
           </ul>
           
   </body>
   </html>
   ```

   

8. 다음 

   ```python
   # views.py
   def student(request, name):
       return render(request, 'student.html', {'name': name})
   
   # urls.py
   from django.contrib import admin
   from django.urls import path
   from pages import views
   
   urlpatterns = [
       path('student/<str:name>/', views.student),
       path('admin/', admin.site.urls),
   ]
   ```

9. sdf

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
   </head>
   <body>
       <h1>이름: {{ name }}!</h1>
       <h2>나이: 28</h2>
   </body>
   </html>
   ```

   