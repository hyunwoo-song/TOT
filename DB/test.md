```python
# TemplateSytaxError

{% load bootstrap4 %}

# fobbiden
{% csrf_token %}

# Page not found
주소와 관련된 문제
urls.py
base.html

# NameError at /nwith/
name 'user' is not defined
view.py 

# IntegrityError at /posts/10/comments/create/
NOT NULL constraint failed: posts_comment.post_id
1:N 관계
views.py
comment.post.id = post_id

or 

post = get_object_or_404(Post, id=post_id)

	comment.post_id = post_id
    
# HTTP ERROR 405
@require_POST
_post.html
form 에 method ="POST" 추가

# NoReverseMatch at /posts/explore/
Reverse for 'comment' not found. 'comment' is not a valid view function or pattern name.
매칭되는 주소가 없다
  <form action="{% url 'posts:comment' post.id %}" method="POST">를 
    <form action="{% url 'posts:comment_create' post.id %}" method="POST">
urls.py 이름을 잘못 지엇거나
잘못 사용했거나 

# field error	
form.py 에서 클래스확인

#OperationalError at [URL]
no such column: movies_score.movie_id
    makemigration
    migrate

1번 2번 
blank=True


{% block ____ 이름을 같게%}



LANGUAGE_CODE = 'Asia-ko'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
```

