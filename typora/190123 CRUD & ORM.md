#  190123 CRUD & ORM

###  CRUD

| 이름                 | 조작            | SQL    |
| -------------------- | --------------- | ------ |
| Create               | 생성            | INSERT |
| Read(또는 Retrieve)  | 읽기(또는 인출) | SELECT |
| Update               | 갱신            | UPDATE |
| Delete(또는 Destroy) | 삭제(또는 파괴) | DELETE |



###  Object-relational mapping





```shell
#가상환경 설정
pyenv virtualenv 3.6.7 orm-venv
pyenv local orm-ven
pip install -U pip
pip install flask Flask-SQLAlchemy Flask-Migrate

```



```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#flask
app = Flask(__name__)

#sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy 초기화
db = SQLAlchemy(app)

# migrate 초기화
migrate = Migrate(app, db)

# table 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)
```



```sqlite
flask db init
flask db migrate
flask db upgrade
python
```

```python
from app import db, User

#Create
#INTSERT INTO users (username, email) VALUES ('Hyunwoo-Song', 'gerrar486@gmail.com')
user = User(username='Hyunwoo-Song', email='gerrar486@gmail.com')
db.session.add(user)
db.session.commit()
User.query.all() #all에 반환되는 값은 복수


user = User(username='admin', email='admin@example.com')
db.session.add(user)
db.session.commit()


user = User(username='apple', email='apple@example.com')
db.session.add(user)
db.session.commit()
# Read
# SELECT * FROM users;
users = User.query.all() 
users

# SELECT * FROM users WHERE username='Hyunwoo-Song';
users = User.query.filter_by(username='Hyunwoo-Song').all()
users
## 결과값 [<User 1>]

# SELECT * FROM users WHERE username='Hyunwoo-Song' LIMIT 1;
users = User.query.filter_by(username='Hyunwoo-Song').first()
users
## 결과값 <User 1>

# 검색 결과가 없다면
user = User.query.filter_by(username='aaaa').first()
user
print(user)
## 결과값 None

# SELECT * FROM users WHERE id=2 LIMIT 1;
user = User.query.get(2) # primary key값만 가져 올 수 있음.
user
## 결과값 <User 2: admin, admin@example.com>

user.email
## 결과값 'admin@example.com'

# SELECT * FROM users WHERE email LIKE '%water%';
users = User.query.filter(User.email.like('%water%')).all()
users
## 결과값 []

users = User.query.filter(User.email.like('%486%')).all()
users
[<User 1: Hyunwoo-Song, gerrar486@gmail.com>]

# ORDER
# users = User.query.order_by(User.username).all()

# LIMIT
# users = User.query.limit(1).all()

# OFFSET
# users = User.query.offset(2).all()

# ORDER + LIMIT + OFFSET
# users = User.query.order_by(User.username).limit(1).offset(2).all()

# DELETE
# DELETE FROM users WHERE id=1;
user = User.query.get(1)
db.session.delete(user)
db.session.commit()

User.query.all()
## 결과값 [<User 2: admin, admin@example.com>, <User 3: apple, apple@example.com>]

# UPDATE
user = User.query.get(2)
user.username
## 결과값 'admin'
user.username = 'google'
user.username
## 결과값 'google'
db.session.commit()
user.query.all()
## 결과값 [<User 2: google, admin@example.com>, <User 3: apple, apple@example.com>]
```



