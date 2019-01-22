#  15 Homework

### 1.우리가사용하는SQLite는 RDBMS에속한다. RDBMS의 특징을2가지만작성하세요.

업무 변화에 대한 적응력 높아 변화하는 업무에 쉽게 활용하며 유지보수 편리하다

테이블의 각 행은 기본 키라고 부르는 고유 식별자로 표시할 수 있고 여러 테이블에 있는 행들은 외래 키를 사용하여 상호 연결될 수 있습니다. 




  



###  2.True False

​	2.1. RDBMS를조작하기위해서는SQL문을사용한다.[True ]
​	2.2. SQL에서명령어는대문자로써야만동작한다.[False]
​	2.3. 일반적인SQL문에서명령어는세미콜론(;) 으로끝난다.[True]
​	2.4. SQLite에서dot(.)으로시작하는명령어는SQL이아니다.[True]
​	2.5. 한개의DB에는한개의테이블만존재한다. [False]	
​	







### 3.다음코드의실행결과로나타나는값을작성하세요.

​	sqlite> .nullvalue 'NULL'
	sqlite> CREATE TABLE ssafy (
		…> id INTEGER,
		…> location TEXT,
		…> class INTEGER
		…> );
sqlite> INSERT INTO ssafy (id, location)
		…> VALUES (1, 'JEJU');
sqlite> SELECT class FROM ssafy WHERE id=1;

```sqlite
class
---------
NULL
```

