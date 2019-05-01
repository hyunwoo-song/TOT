# Read Me

### 1. 가상환경 설정

```bash
pyenv virtualenv 3.6.7 money
pyenv local money
pip install django==2.1.8
```



### 2. project & app 설정

```bash
django-admin startproject GSM .
./manage.py startapp movies
```

### 3. urls.py 생성

```python
# 기존의 urls.py
from django.contrib import admin
from django.urls import path, include # < --- 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')), # < --- 추가
]

# app폴더내 urls.py 생성
# app폴더내 urls.py 

from django.urls import path, include
from . import views 

app_name = 'movies'

urlpatterns = [
    
]

```

### 4. models.py

```python
# models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    genre = models.CharField(max_length=100)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

# bash
./manage.py makemigrations
./manage.py migrate
```

### 5. admin 생성

```python
# bash
./manage.py createsuperuser

# admin.py에 모델 적용
from django.contrib import admin
from .models import Movie			# <--- 추가

admin.site.register(Movie)			# <--- 추가
```

### 6. base.html 생성

```python
# 프로젝트 폴더 내 templates 폴더 생성
# 그 폴더 내 base.html 파일 생성
```

```html
<!--base.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {% block container %}
    {% endblock %}
</body>
</html>
```

```python
# settings.py
 'DIRS': [os.path.join(BASE_DIR, 'GSM', 'templates')],
```



## 세부내용

### 1. 영화목록

```python
# urls.py
path('', views.list, name='list')

# views.py
from .models import Movie

def list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {'movies':movies})
```

```html
{% extends 'base.html' %}
{% block container %}
<h1>여기는 list다 오바</h1>
{% for movie in movies %}
<h3>Title:<a href="{% url 'movies:detail' movie.id %}">{{movie.title}}</a></h3>
<h5>Score:{{movie.score}}</h5>
{% endfor %}
{% endblock %}
```

### 2. 영화 정보 조회

```python
# urls.py
path('<int:movie_id>/', views.detail, name='detail'),

# views.py
from django.shortcuts import get_object_or_404
def detail(request, movie_id):
    movie = get_object_or_404(Movie, id= movie_id)
    return render(request, 'movies/detail.html', {'movie':movie})
```

```html
<!--detail.html-->
{% extends 'base.html' %}
{% block container %}
<h3>Title: {{movie.title}}</h3>
<p>관객수:{{movie.audience}}</p>
<p>평점:{{movie.score}}</p>
<p>장르:{{movie.genre}}</p>
<p>주소:{{movie.poster_url}}</p>
<p>평:{{movie.description}}</p>

<a href="">목록</a>
<form>
    <input type="text" name=""/>
    <input type="submit" value="수정"/>
</form>
<a href="{% url 'movies:delete' movie.id %}">삭제</a>
{% endblock %}
```

### 2-2 영화정보 조회 (삭제, 수정, 목록)

#### 2-2-1 목록

```html
<!--detail.html-->
<a href="{% url 'movies:list' %}">목록</a>

```

#### 2-2-2 삭제

```html
<!--detail.html-->
<a href="{% url 'movies:delete' movie.id %}">삭제</a>

```

```python
# urls.py
path('<int:movie_id>/delete/', views.delete, name='delete'),

# views.py
def delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movies:list')
```

#### 2-2-3 수정

```html
<!--detail.html-->
<a href="{% url 'movies:update' movie.id %}">수정</a>
```

```python
# urls.py
path('<int:movie_id>/update/', views.update, name='update'),

# views.py
def update(request, movie_id):
    movie = get_object_or_404(Movie, id= movie_id)
    if request.method =="POST":
        movie_form = MovieForm(instance= movie, data = request.POST)
        if movie_form.is_valid():
            movie_form.save()
        return redirect('movies:detail' , movie_id)

    else:
        movie_form = MovieForm(instance=movie)
        return render(request, 'movies/form.html', {'movie_form':movie_form})
    
```



### 3.영화 정보 삭제

```python
# urls.py
path('<int:movie_id>/delete', views.delete, name='delete'),

# views.py
from django.shortcuts import redirect
def delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movies:list')
```



### 4. 평점

#### 4.1 평점 생성 & 목록

```html
<!--detail.html-->
<form action="{% url 'movies:score_new' movie.id %}" method="POST">
    {% csrf_token %}
    {{ score_form }}
    <input type="submit" value="submit"/>
</form>
```

```python
# urls.py
path('<int:movie_id>/scores/new/', views.score_new, name='score_new'),

# views.py
def score_new(request, movie_id):
    score_form = ScoreForm(request.POST)
    if score_form.is_valid():
        score = score_form.save(commit=False)
        score.movie_id = movie_id
        score.save()
    return redirect('movies:detail', movie_id)
```

```html
<!--detail.html-->
{% for score in movie.score_set.all %}
<p>{{score.content}} : {{score.score}}</p>
<a href="{% url 'movies:score_delete' movie.id score.id %}">삭제</a>
{% endfor %}
```



#### 4.2 평점 삭제

```python
# urls.py
path('<int:movie_id>/scores/<int:score_id>/delete/', views.score_delete, name='score_delete'),

# views.py
def score_delete(request, movie_id, score_id):
    score = get_object_or_404(Score, id=score_id)
    score.delete()
    return redirect('movies:detail', movie_id )

```



### 5. Account

#### 5.1 모델링

```python
# models.py(accounts)
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

# models.py(movies)
from django.conf import settings

class Score(models.Model):
    content = models.CharField(max_length=100)
    score = models.IntegerField(blank=True)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE) 
    # 추가
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
```
```python
# settings.py
	AUTH_USER_MODEL = 'accounts.User'
```

```bash
# bash
./manage.py makemigrations
./manage.py migrate
```



#### 5.2 계정 목록

```python
 # urls.py 
    path('', views.list, name='list'),
    
 # views.py
	from .models import User
    
	def list(request):
    users= User.objects.all()
    return render(request, 'accounts/list.html', {'users':users})

```

``` html
<!--list.html-->
{% extends 'base.html' %}
{% block container %}
<h1>User List</h1>
{% for user in users %}
<h3><a href="{% url 'accounts:detail' user.id %}">{{ user.username }}</a></h3>
{% endfor %}
{% endblock %}
```

#### 5.3 계정 세부 정보

```python
# urls.py 
	path('<int:user_id>/', views.detail, name='detail'),
    
# views.py
    def detail(request, user_id):
        person = User.objects.get(pk=user_id)
        return render(request, 'accounts/detail.html', {'person':person})
```

```html
<!--detail.html-->
{% extends 'base.html' %}
{% block container %}
<h1>여기는 디-----테일</h1>

<h3>유저명 : {{person.username}}</h3>
<p>e-mail : {{person.email}}</p>
{% endblock %}
```



#### 5.4 회원가입

```python
# urls.py
	path('signup/', views.signup, name='signup'),
    
# forms.py
	from django import forms
	from django.contrib.auth import get_user_model
	from django.contrib.auth.forms import UserCreationForm
    
	class UserCreateForm(UserCreationForm):
        class Meta:
            model = get_user_model()
            fields = ('username', 'email',)
            
# views.py
	from django.views.decorators.http import require_http_methods
    from django.contrib.auth import login as auth_login
    from .forms import UserCreateForm
    
	@require_http_methods(["GET", "POST"])    
    def signup(request):
        if request.user.is_authenticated:
            return redirect('movies:list')
        if request.method == "POST":
            user_form = UserCreateForm(request.POST)
            if user_form.is_valid():
                user = user_form.save()
                auth_login(request, user)
                return redirect('movies:list')
        else:
            user_form = UserCreateForm()
        return render(request, 'accounts/form.html', {'user_form':user_form})

```

```html
<--!form.html-->
    {% extends 'base.html' %}
    {% block container %}
    <form method="POST">
        {% csrf_token %}
        {{ user_form }}
        <input type="submit" value="Submit"/>
    </form>

    {% endblock %}
```



#### 5.5 login

```python
# urls.py
	path('login/', views.login, name='login'),
    
# views.py
	from django.contrib.auth.forms import AuthenticationForm
    
	def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
        
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        user_form = AuthenticationForm()
    return render(request, 'accounts/form.html', {'user_form':user_form})
```



#### 5.6 logout

```python
# urls.py
	path('logout/', views.logout, name='logout'),
    
# views.py
	from django.contrib.auth import logout as auth_logout
    
	@login_required
    def logout(request):
        auth_logout(request)
        return redirect('movies:list')
```



#### 5.7 팔로우


```python
# urls.py 
	path('<int:user_id>/follow/', views.follow, name='follow'),
    
# views.py
	from django.contrib.auth import get_user_model
	from django.shortcuts import get_object_or_404
    
	@login_required
	def follow(request, user_id):
        person = get_object_or_404(get_user_model(), id=user_id)

        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
        return redirect('accounts:detail', person.id)
 
```

```html
<!--detail.html-->
{% extends 'base.html' %}
{% block container %}
<h1>여기는 디-----테일</h1>

<h3>유저명 : {{person.username}}</h3>
<p>e-mail : {{person.email}}</p>

<!-- 추가 -->
{% if user != person %}
    {% if user in person.followers.all %}
    <a href="{% url 'accounts:follow' person.id %}">un팔</a>
    {% else %}
    <a href="{% url 'accounts:follow' person.id %}">팔</a>
    {% endif %}
{% endif %}

{%for score in person.score_set.all %}
{{score.content}}
{{score.score}}
{% endfor %}

<p>팔로워수 {{person.followers.count}}</p>
<p>팔로잉수 {{person.followings.count}}</p>


{% if user == person %}
{{ maxscore }}
{{ mmother }}
{% endif %}
{% endblock %}

```



```python
		<a href="{% url 'accounts:logout' %}">로그아웃</a>   
    {% else %}
        <a href="{% url 'accounts:signup' %}">회원가입</a>
        <a href="{% url 'accounts:login' %}">로그인</a>
        
```

