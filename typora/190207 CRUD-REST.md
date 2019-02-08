# 190207

d/ rwx/ r-x/ r-x

d: directory(Folder)

rwx :  파일의 소유자 read write 모두 할 수 있음

r -x: 그룹에 속한 사람들 읽고 실행하기

r-x: 그 외의 사람들



`crud` 폴더에 `templates` 폴더 생성 그안에 `base.html` 생성

`crud` 폴더에 `setting.py`로 가서 

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')],
```



`base.html`

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
    <h1>여기는 base.html</h1>
    {% block _____ %}
    {% endblock %}
</body>
</html>
```



`앱폴더`에서 `templates` 에서 `index.html`

```html
나머지 다 지우고

{% extends 'base.html' %}
{% load static %}
{% block container %}

    <img src="{% static '12312.png' %}"></img>
    <h1>Post Index </h1>
    <a href="{% url 'posts:new'%}">New</a>
    <ul>
    {% for post in posts %}
        <li> <a href="{% url 'posts:detail' post.pk %}">{{ post.title }} - {{ post.content }}</a></li>
    {% endfor %}
    </ul>
    
{% endblock %}
```



```bash
서버 열기 
python manage.py runserver $IP:$PORT
```



`앱폴더`에서 `templates` 에서 `new.html`

```html
{% extends 'base.html' %}

{% block container %}
    <body>
        <form action="{% url 'posts:create' %}" method="post" enctype="multipart/form-data">   
            {% csrf_token %}
            <input type="text" name="title"/>      
            <input type="text" name="content"/> 
            <input type="file" name="image" accept="image/*"/>
            <input type="submit" value="Submit"/>
        </form>
    </body>
{% endblock %}
```



`앱폴더`에서 `templates` 에서 `edit.html`

```html
{% extends 'base.html' %}
{% block container %}

    <h1>Post Edit</h1>
    <form action="{% url 'posts:update' post.pk %}" method="post">
        {% csrf_token %}
        <input type="text" name="title" value="{{ post.title }}"/>
        <input type="text" name="content" value="{{ post.content }}"/>
        <input type="submit" value="Submit"/>
    </form>
{% endblock %}

```



`앱폴더`에서 `templates` 에서 `detail.html`

```html
{% extends 'base.html' %}

{% block container %}

    <h1>Post detail</h1>
    <img src="{{ post.image.url }}"></img>
    <h2>Title : {{ post.title }}</h2>
    <p>content : {{ post.content }}</p>
    <a href="{% url 'posts:list' %}">List</a>
    <a href="{% url 'posts:edit' post.pk %}">edit</a>
    <a href="{% url 'posts:delete' post.pk %}">Delete</a>
    
    
    <hr>
    
    <form action='{% url "posts:comments_create" post.pk %}' method='post'>
        {% csrf_token %}
        댓글 : <input type="text" name="content"/>
        <input type="submit" value="Submit"/>
    </form>
    
    <ul>
        {% for comment in post.comment_set.all %}
            <li>{{ comment.content }} - <a href="{% url 'posts:comments_delete' post.pk comment.pk %}">Delete</a> </li>
        {% endfor %}
    </ul>
    
    
{% endblock %}
```





## REST의 구성

* 자원(Resource) -URI
* 행위(Verb) - HTTP Method
* 표현(Representations)



## REST API 디자인 가이드

1. URI는 정보의 자원을 표현해야 한다.
2. 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다.



## 예시

```
GET /movies/show/ 1    (X)
GET /movies/1		   (O) 		
```

```
GET /movies/create      (X) - GET Method는 자원 생성에 부적합
POST /movies            (O)
```

```
GET /movies/2/update    (X) - GET 부적합
PUT /movies/2           (O)
```



`앱폴더` `urls.py`

```python
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='list'), # GET
    path('new/', views.new, name='new'), # GET(new), POST(create)
    # path('create/', views.create, name='create'),
    path('<int:post_id>/', views.detail, name='detail'), # GET
    path('<int:post_id>/delete/', views.delete, name='delete'), # GET(confirm), POST(delete)
    path('<int:post_id>/edit/', views.edit, name='edit'), # GET(edit), POST(update)
    # path('<int:post_id>/update/', views.update, name='update'),
    # path('naver/<str:q>/', views.naver, name='naver'),
    # path('github/<str:username>/', views.github, name='github'),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
    
]
```

`views.py`

```python
# Create your views here.
def new(request):
    if request.method == 'POST':
        #create
        title = request.POST.get('title') 
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        post = Post(title=title, content=content, image=image)
        post.save() 
        return redirect('posts:detail', post.pk)
    else:
        return render(request, 'new.html')
    
```

`new.html`

```html
{% extends 'base.html' %}

{% block container %}
    <body>
        <form method="post" enctype="multipart/form-data">   # 액션을 지워준다
            {% csrf_token %}
            <input type="text" name="title"/>      
            <input type="text" name="content"/> 
            <input type="file" name="image" accept="image/*"/>
            <input type="submit" value="Submit"/>
        </form>
    </body>
{% endblock %}

```



`views.py`

```python
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        # update
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:detail', post.pk)
    else:
        # edit
        return render(request, 'edit.html', {'post':post})
    
```

`edit.html`

```html
{% extends 'base.html' %}
{% block container %}

    <h1>Post Edit</h1>
    <form method="post"> # action을 지운다
        {% csrf_token %}
        <input type="text" name="title" value="{{ post.title }}"/>
        <input type="text" name="content" value="{{ post.content }}"/>
        <input type="submit" value="Submit"/>
    </form>
{% endblock %}


```





`앱폴더`의 `templates`폴더 내 `delete.html` 생성

`views.py`

```python
def delete(request, post_id):
    if request.method == 'POST':
        # 삭제하는 코드
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect("posts:list")
    else:
        return render(request, 'delete.html')
```

`delete.html`

```html
{% extends 'base.html' %}

{% block container %}

    <h1>Post detail</h1>
    <img src="{{ post.image.url }}"></img>
    <h2>Title : {{ post.title }}</h2>
    <p>content : {{ post.content }}</p>
    <a href="{% url 'posts:list' %}">List</a>
    <a href="{% url 'posts:edit' post.pk %}">edit</a>
    <a href="{% url 'posts:delete' post.pk %}">Delete</a>
    
    
    <hr>
    
    <form action='{% url "posts:comments_create" post.pk %}' method='post'>
        {% csrf_token %}
        댓글 : <input type="text" name="content"/>
        <input type="submit" value="Submit"/>
    </form>
    
    <ul>
        {% for comment in post.comment_set.all %}
            <li>{{ comment.content }} - <a href="{% url 'posts:comments_delete' post.pk comment.pk %}">Delete</a> </li>
        {% endfor %}
    </ul>
    
    
{% endblock %}

```

