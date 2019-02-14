#  Django 프로젝트 만들기

### 1. Django 프로젝트 생성

- 프로젝트를 만들고자 하는 폴더로 이동
- django-admin startproject <프로젝트이름>

```bash
# 가상환경 설치시 이거 부터
pyenv virtualenv 3.6.7 intro-venv
pyenv local intro-venv

#장고 설치
pip install django

#프로젝트를 시작하겠다
django-admin startproject intro .
```



### 2. **Django 서버 실행**

- 앞에서 생성했던 <프로젝트이름> 디렉토리로 이동
- python manage.py runserver $IP:$PORT	

### 3. App 만들기

- 프로젝트 폴더로 이동
- python manage.py startapp <앱이름>
- ls 명령어를 치면 <앱이름>이라는 디렉토리가 생성되어 있음



### 4. **hello world를 출력하는 index 함수 만들기**

- 앞에서 생성한 <앱이름> 폴더로 이동
- views.py(\프로젝트이름\앱이름\views.py) 수정 - 페이지 요청에 대해 hello world라는 httpResponse

```python
# views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world")
```



### 5. **앱에 접근할 조건을 지정하는 함수 만들기**

- \프로젝트명\프로젝트명\urls.py에 urlpatterns 수정

```python
# urls.py
from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')), # include는 앱접속을 위해 사용
]
```



###  6. **앞서 생성한 index 함수를 실행할 조건을 지정하는 함수 만들기**

- 앞서 생성한 <앱이름> 폴더로 이동

- urls.py(\프로젝트이름\앱이름\urls.py) 파일 생성

- urls.py에 urlpatterns로 index함수를 지정

  ```python
  from django.urls import path, include
  from . import views
  
  urlpatterns = [
      path('', views.index),
  ]
  ```



### 7. app과 관련된 정보를 저장할 model

- 모델클래스는 앱 안의 models.py에 정의합니다.

- 모델 class는 `models.Model`을 상속받아야 합니다.
- 모델 class안의 멤버 변수의 field에 대한 정보는 [Field types](https://docs.djangoproject.com/es/1.9/ref/models/fields/#field-types)를 참고해주세요

```python
# models.py
from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=10) # CharField는 초기값 설정필수 
    introduction = models.TextField()
    area = models.CharField(max_length=15) 
    party_number = models.IntegerField(default=1)
```



### 8. 마이그레이션과 DB

- mysite/settings.py - INSTALLED_APPS 리스트에 elections(앱이름) 추가

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps'  				# 추가
]
```

- mysite 폴더로 이동 후 `python manage.py makemigrations` 입력
- `python manage.py migrate`로 DB에 공간 만들기



### 9. admin

1. admin 사용자 만들기
   - 프로젝트 폴더로 이동
   - python manage.py createsuperuser 실행
   - 유저 이름과 email, password 설정
2. 서버 실행
   - python manage.py runserver
3. admin으로 접속
   - 브라우저에서 admin:localhost:8000/admin으로 접속
   - 1에서 만든 사용자로 접속

### 10-1. Candidate 등록

1. app폴더의 admin.py에 model에서 정의한 Candidate를 regist

   ```python
   # admin.py
   from django.contrib import admin
   
   from .models import Candidate
   
   # Register your models here.
   admin.site.register(Candidate)
   ```

   

2. 브라우저를 새로고침 하면 Candidate가 반영됩니다.

3. Candidate - ADD CANDIDATE - 내용을 추가하고 SAVE -> object가 추가됩니다.



### 10-2.  object를 구분하는 방법

- python에서는 object를 표현하는 문자열을 정의할 때는 `__str__`메소드를 오버라이딩합니다. 예를 들어 위에서 등록한 Candidate의 이름으로 object를 표현하고 싶은 경우,

  ```python
  # models.py
  
  from django.db import models
  
  # Create your models here.
  class Candidate(models.Model):
      name = models.CharField(max_length = 10)
      introduction = models.TextField()
      area = models.CharField(max_length = 15)
      party_number = models.IntegerField(default = 0)
  
      def __str__(self):					# 추가
          return self.name
  ```

  로 수정한 후, 브라우저를 새로고침 하면 후보자 이름이 보입니다.



### 11. 데이터 보여주기

####  DB에 모델이 저장된 구조

Candidate 테이블에서 각 데이터 필드는 column(열)으로, 각 Candidate의 정보는 row(행)으로 저장되어 있습니다.

####  데이터에 접근하는 방법

Candidate 테이블에 등록한 정보를 보기 위해서는

```python
# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate    # 추가 

# Create your views here.
def index(request):
    candidates = Candidate.objects.all() 
    str=''
    for candidate in candidates:
        str += f"<p>{candidate.name}기호 {candidate.party_number}번({candidate.area})<br>"
        str += candidate.introduction+"</p>"
    return HttpResponse(str)
```



### 12. shell에서 직접 DB에 요청

#### shell 실행방법

1. manage.py가 있는 폴더로 이동 후
2. python manage.py shell

####  DB에 요청하기

1) **기본** - 사용할 모델 클래스 import

```bash
>>> from elections.models import Candidate
```

2) **모든 객체 불러오기** - [all()](https://docs.djangoproject.com/en/1.9/ref/models/querysets/#all)

```bash
>>> Candidate.objects.all()
```

3) **새 객체 생성하고 저장하기** - [Model.save()](https://docs.djangoproject.com/en/1.9/ref/models/instances/#django.db.models.Model.save)

```bash
>>> new_candidate = Candidate(name = "루비오") #생성만 한 상태. 아직 저장되지 않음
>>> new_candidate.save() #new_candidate가 DB에 저장됨
```

4) **특정 조건을 만족하는 객체 불러오기** - [filter()](https://docs.djangoproject.com/en/1.9/ref/models/querysets/#filter)

```bash
>>> no1 = Candidate.objects.filter(party_number = 1) #party_number = 1인 객체를 리스트 형태로 return
>>> no1[0].party_number #리스트 형태이기 때문에 index로 접근
>>> no1[0].name
```



### 13. 템플릿으로 html 불러오기

1. 앱(elecetions) 폴더 아래에 templates 폴더 생성 (C\Code\mysite\elections\templates)
2. templates 폴더 아래 elecetions 폴더 생성
3. elecetions 폴더 아래 index.html 파일 생성
4. index.html 과 views.py 수정

```python
# views.py
def index(request):
    candidates = Candidate.objects.all()
    return render(request, 'apps/index.html') # 수정
```



### 14. 템플릿에 정보 채우기

1. views.py에서 DB에 있는 후보 정보를 html에 전달

```python
# views.py

def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request, 'apps/index.html', context)
```

```html
<!--index.html-->
<tbody>
        {% for candidate in candidates %}
        <tr>
            <td> {{candidate.name}} </td>
            <td> {{candidate.introduction }}</td>
            <td> {{ candidate.area }}</td>
            <td> 기호 {{ candidate.party_number }} 번</td>
        </tr>
        {% endfor %}
<tbody>
```



### 15. MVC 패턴(Model View Controller Pattern)

#### Model(데이터) - models.py

- Candidate 클래스의 형식대로 데이터를 DB에 저장, 불러옴

#### View(화면) - templates

- 화면에 어떤 장면을 보여줄지를 결정

#### Controller(조율) - views.py

- Candidate 모델에서 데이터를 읽어, index.html에 전달



### 16. 여론조사 모델

#### 1. 새로운 모델을 models.py에 정의합니다.

```python
# models.py
class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length=15)

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE) 
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    votes = models.IntegerField(default = 0)
    
    # on_delete 옵션
	# 1. CASCADE : 부모가 삭제되면, 자기 자신도 삭제.
    # 2. PROTECT : 자식이 존재하면, 부모 삭제 불가능.
    # 3. SET_NULL : 부모가 삭제되면, 자식의 부목 정보에 NULL
    
```

#### 2. admin에서 Poll 모델을 사용하기 위해, admin.py에 Poll을 등록(regist)합니다.

```python
# admin.py
from .models import Candidate, Poll

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Poll)
```

#### 3. 모델 등록

migration 파일을 만든 후 - migration 파일을 DB에 반영 - runserver 과정을 밟습니다.

powershell 등에서 manage.py가 있는 디렉토리로 이동 후,

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver

브라우저에서 localhost:8000/admin으로 접속하면 Poll을 등록할 수 있습니다.



#### [DateTimeField](https://docs.djangoproject.com/en/1.9/ref/models/fields/#datetimefield)

date(날짜)와 time(시간)을 나타내며, python의 datetime.datetime 인스턴스로 표현됩니다.

#### [CharField](https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.CharField)

string을 나타내며, 필수 인자 max_length가 있습니다.
길이가 긴 문자열을 저장하려면 [TextField](https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.TextField) 등을 쓰세요.

- [CharField.max_length](https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.CharField.max_length) : 해당 필드의 최대길이를 설정합니다. 예를 들어 5로 설정하면 5글자 이하로만 저장할 수 있습니다.

#### [IntegerField](https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.IntegerField)

정수를 나타냅니다.
이 필드는 Django가 지원하는 모든 데이터 베이스에서 -2147483648에서 2147483647까지의 정수를 안전하게 저장합니다.
더 큰 정수는 [BigIntegerField](https://docs.djangoproject.com/en/1.9/ref/models/fields/#bigintegerfield) 등을 이용하세요.

#### [ForeignKey](https://docs.djangoproject.com/en/1.9/ref/models/fields/#foreignkey)

한 모델에서 다른 모델을 이용할 때에 씁니다(보통 many-to-one 관계 모델에서 이용합니다).

영상에서도 여론조사(Poll) id 하나에 여러 개의 [후보-득표수]를 저장합니다.



### 17. url 다루기

#### 링크 만들기

href 어트리뷰트로 link 주소를 설정합니다. 지역구가 출력되는 곳에 링크를 추가하려면,

```html
<!--html-->
.
.
.
<tr>
            <td> {{candidate.name}} </td>
            <td> {{candidate.introduction }}</td>
            <td> <a href = "areas/{{ candidate.area }}/">{{ 							candidate.area }}</a></td>
            <td> 기호 {{ candidate.party_number }} 번</td>
        </tr>
```

localhost:8000/areas/미국/에 대한 url을 등록해주지 않았기 때문에 링크를 클릭하면 페이지를 찾을 수 없다는 창이 뜹니다.(Page not found)

url을 등록하려면 urls.py와 views.py를 수정합니다.

```python
# urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('areas/<str:area>/', views.areas)
]

# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate

# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request, 'apps/index.html', context)

def areas(request, area):
    return HttpResponse(area)
```



