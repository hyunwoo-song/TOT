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
