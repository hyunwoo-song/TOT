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