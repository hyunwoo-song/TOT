#   14 Homework

* Django는 요청에 대한 응답을 해줄 때 허용하는 도메인에게만 응답을 해주도록 설정한다.

  Settings.py파일에서도메인을허용하기위해수정해줘야하는변수이름을찾아서적어주세요

  ```python
  ALLOWED_HOSTS = ['playground-tot23.c9users.io'] 추가
  
  INSTALLED_APPS = [
      'pages.apps.PagesConfig', <------추가
  ]
  ```

  

* https://<your-server-url>/ssafy 로요청이들어왔을때응답을해주기위해urls.py에추가해주어야할코드를작성하세요(실행하는함수는views.py안에있는ssafy 함수라고가정한다.)

  ```python
  from pages import views 
  
  urlpatterns = [
      path('index/', views.index),
      path('admin/', admin.site.urls),
  ]
  ```

  

* Django 서버를실행시키는명령어를작성해주세요(C9환경에서)

  ```bash
  # 서버실행 명령어
  python manage.py runserver $IP:$PORT
  ```

  

* django는MTV로이루어진web framework 이다.MTV가무엇의약자인지작성하세요

  ```
  M: model
  T: template
  V : view
  ```

  

