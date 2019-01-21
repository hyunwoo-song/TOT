# DAY04 python

### dict.py

```python
# 1. 딕셔너리 만들기
lunch = {
    '중국집':'02-1123-4544',
    '양식집':'053-216-4545',
    '한식집':'054-451-5452',
}

dinner = dict(중국집='02-1233-4544') #딕셔너리로 변환시켜주는 내장함수 # key값은 문자열이 아닌 양쪽 따옴표 없이 기입
# int()
# list()


# 2. 딕셔너리 내용 추가하기
lunch['분식집'] = '053-123-4567'


# 3. 딕셔너리 내용 가져오기
print(lunch['중국집']) #=> 02-1123-4544
idol = {
    'BTS': {
        '지민':24,
        'RM': 25,
    }
}

idol['BTS']       #=> dit -> { '지민':24, 'RM':25 }
idol['BTS']['RM'] #=> 25


# 4. 딕셔너리 반복문 활용하기
# 기본 활용
for key in lunch:
    print(key) #=> key
    print(lunch[key]) #=> value

# key만 가져오기 : .keys()
for key in lunch.keys():
    print(key)

# value만 가져오기 : .values()
for value in lunch.values():
    print(value)

# item (key, value) 가져오기 : .items()
# lunch.items() #=> [('중식','02'), ... ]
for item in lunch.items():
    print(item[0], item[1])
# 말고 item을 쪼개서 넣을 수 있다.
# for key, value in lunch.items():
#     print(key, value)

# n개 = 자료형 길이 n (같을경우 가능)
a, b, c = (1,2,3)
print(a)
print(b)


# 1. 이 학생의 평균을 구하시오.
total_score = 0
for subject_score in score.values():
    total_score = total_score + subject_score
    
ave_score = total_score / len(score)
print(ave_score) 

# sum은 바로 사용할 수 없다. 내장함수로 다른기능으로 등록되어있기 때문이다.

# 1.2 두번째 풀이
total_score = sum(score.values()) # sum([80, 90, 100]) => 270
ave_score = total_score / len(score)
print(ave_score) 

```



### Quiz 1

```python
# 문제
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100,
}
# 1. 이 학생의 평균을 구하시오.
total_score = 0
for subject_score in score.values():
    total_score = total_score + subject_score
    
ave_score = total_score / len(score)
print(ave_score) 

# sum은 바로 사용할 수 없다. 내장함수로 다른기능으로 등록되어있기 때문이다.

# 1.2 두번째 풀이
total_score = sum(score.values()) # sum([80, 90, 100]) => 270
ave_score = total_score / len(score)
print(ave_score) 
```



### Quiz 2

``` python
# 문제 2. 반 평균을 구하시오.

scores = {
            'a': {
                    '수학': 80,
                    '국어': 90,
                    '음악': 100,
                 },
            'b': {
                    '수학': 80,
                    '국어': 90,
                    '음악': 100,
                 }
         }

total_scores = 0 #=> 80 + 90 + 70
count = 0 #=> 1 + 1 + 1

for person_scores in scores.values(): #=> [{'수학': 80, '국어': 90, '음악': 100}, {'수학': 80, '국어': 90, '음악': 100}]
    person_scores #=>{'수학': 80, '국어': 90, '음악': 100}
    person_scores.values() # =>[80, 90, 70]
    for subject_scores in person_scores.values():
        # 3번째 시행
        # subject_scores #=> 70
        total_scores += subject_scores
        count += 1

avg_scores = total_scores/count   
print(avg_scores)

```



### Quiz 3

``` python
# 문제 3. 도시별 최근 3일의 온도입니다.

city = {
        '서울': [-6, -10, 6],
        '대전': [-3, -6, 2],
        '광주': [-0, -2, 10],
        '구미': [2, -2, 9],
        }

# 3-1. 도시별 최근 3일의 온도 평균은?
# '''
# 출력 예시)
# 서울 : 값
# 대전 : 값
# 광주 : 값
# 구미 : 값
# '''



# for key in city.keys():
#     avg_temp =sum(city[key])/len(city[key])
    # print(f'{key}:{avg_temp}')


for name, temp in city.items(): # city.items() #=>[('서울': [-6, -10, 6]), ...]
    name #=> '서울'
    temp #=> [-6, -10, 6]
    # 1. 반복
    total_temp = 0 #=> -10
    for t in temp:
        # 1번째 시행 
        # t #=> -6
        total_temp += t
    avg_temp = total_temp / len(temp) #=> -10/3
    print(f'{name} : {avg_temp}')

    #2. 내장 함수
    avg_temp = sum(temp) / len(temp) 
    print(f'{name} : {avg_temp}')
```



### dict_advenced.py

```python
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gm":  {
            "lecturer": "junwoo",
            "manager": "pro-gm",
            "class president": "엄윤주",
            "groups": {
                "1조": ["강대현", "권민재", "서민수", "이규진"],
                "2조": ["박재형", "서민호", "윤종원", "이지현"],
                "3조": ["김미진", "김영훈", "엄윤주", "여성우"],
                "4조": ["김교훈", "김유림", "송현우", "이현수", "진민재", "하창언"],
            }
        },
        "gj": {
            "lecturer": "change",
            "manager": "pro-gj"
        }
    }
}
```



#### Q1. 

난이도* 1. 지역(location)은 몇개 있나요? : list length

출력예시) 4

```python
num_location = ssafy["location"]
print(len(num_location))
```



#### Q2.

난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in

출력예시)false

```python
a = ssafy["language"]["python"]["python standard library"]
if a.count('requests') > 0 :
    print('True')
else :
    print('false')
```



####  Q3.

난이도** 3. gm반의 반장의 이름을 출력하세요. : depth 있는 접근

출력예시)

엄윤주

```python
print(ssafy["classes"]["gm"]["class president"])
```



#### Q4.

난이도*** 4. ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복

출력 예시)

python

web

```python
b = ssafy["language"]
for key in b.keys():
    print(f'{key}')
```



#### Q5.

난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복

출력 예시)

change

pro-gj

```python
c = ssafy["classes"]["gj"]
for value in c.values():
    print(f'{value}')
```



#### Q6. 

난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation

출력 예시)

flask는 micro이다.

django는 full-functioning이다.

```python
d = ssafy["language"]["python"]["frameworks"]
for k, v in d.items():
    print(f'{k}는 {v}이다.')
```





#### Q7.

난이도***** 7. 오늘 당번을 뽑기 위해 groups의 4조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.

출력예시)

오늘의 당번은 하창언

```python
import random

e = ssafy["classes"]["gm"]["groups"]
g = []
for k, v in e.items():
    g += v
h = random.choice(g)    

print(f'오늘의 당번은 {h}')
```

```python
import random

e = ssafy["classes"]["gm"]["groups"]
f = random.choice(list(e.items()))
g = random.choice(f[1])
print(f'오늘의 당번은 {g}')
```

