#  190131

```bash
서버 실행 python manage.py runserver $IP:$PORT	
```



앱 폴더 안에 폴더 생성 static

static 폴더 내 style.css 파일 생성

```css
h1 {
    color: red;
}
```



사용하고자 하는 링크로 간다

```html
# ex) index.html

{% load static %}      # static을 임포트 해야한다
<!DOCTYPE html>      

<link rel="stylesheet" href="{% static 'style.css' %}" type="text/css" />

<img src="{% static '12312.png' %}"></img>
```



settings.py

``` python
# settings.py
# os.path 는 Windows: \ 인지 Linux: / 확인 해주는 기능

STATICFILES_DIRS= [
    os.path.join(BASE_DIR, 'crud', 'assets'),
    ]

# BASE_DIR: 최상단 폴더 안에 있는 'crud' 폴더 안에 있는 'assets' 폴더

# crud 파일 안에 assets폴더 생성 그리고 그 폴더 안에 public.css 파일 생성

<link rel="stylesheet" href="{% static 'public.css' %}" type="text/css" />
```

```css
# public.css
h1{
    color: blue;
}
```



앱폴더내 models.py

```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 추가 되는 부분
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # create 될 떄, 딱 한번 현재시각
    updated_at = models.DateTimeField(auto_now=True) # 변경이 될때마다, 현재 시각
    
```

```bash
이미지 올릴때는 pillow 설치


python manage.py makemigrations
1
(엔터치기)
python manage.py migrate
```

```
# DB 초기화 하는 방법
db.sqlite3
migrations 폴더내 000으로 시작하는 파일들 삭제
admin도 삭제 되니 알아둘것
```

```
한국 패치
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

```html
# new.html
<!-- enctype : multipart/form-data (binary 전송 가능(파일같은거 보낼시)) 
				application/x-ww-form-urlencoded (기본값)-->
<form action="{% url 'posts:create' %}" method="post" enctype="multipart/form-data">
    # enctype="multipart/form-date" 추가
<input type="file" name="image" accept="image/*"/> # 추가
```

```python
# views.py
def create(request):
    title = request.POST.get('title') 
    content = request.POST.get('content')
    image = request.FILES.get('image')         # 추가된 부분
    
    post = Post(title=title, content=content, image=image)
    post.save() 
    return redirect('posts:detail', post.pk)
```

```python
# detail.py
<img src="{{ post.image.url }}"></img>

```

```python
# settings.py

# Media Files
MEDIA_URL = '/media/'   # media 부분은 변경가능
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # media 부분은 변경가능
```

```python
# 앱의 url이아니라 프로젝트의  url.py

from django.conf.urls.static import static
from django.conf import settings


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```





```bash
# 장고 이미지 킷 설치
pip install pilkit
pip install django-imagekit pilkit

```

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'imagekit',                 # 추가
    'posts.apps.PostsConfig',   
]

# models.py
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# ResizeToFill : 300, 300 맞추고 넘치는 부분 잘라냄
# ResizeToFit : 300, 300 맞추고 남는 부분을 빈 공간으로 둠.



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 주석하고 밑에껄로 사용
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        	upload_to='posts/images', # 저장위치
            processors=[ResizeToFill(300, 300)], # 처리할 작업 목록
            format='JPEG', # 저장 포맷 (확장자)
            options={'quality':90} # 저장 포맷 관련 옵션
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

```
python manage.py makemigrations
python manage.py migrate

```

