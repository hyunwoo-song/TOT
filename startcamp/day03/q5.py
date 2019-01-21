'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')
# 아래에 코드를 작성해 주세요.
# input : 10;2;3 
# 1. split() 이용
prices = prices.split(';') #=> ['10', '2', '3']
# 2. 반복을 통한 item들 int() 이용

int_prices = [] # or list()
for i in prices:
    int_prices.append(int(i)) # =>[10, 2, 3]          # int(i) # => 10
    
# list(map(함수, 자료형)) -> list( map(int, prices) ) #=> [10, 2, 3] 


# 3. .sort() or sorted() 정렬
int_prices.sort(reverse=True) #=> reverse=True 사용하면[2, 3, 10] -> [10, 3, 2]

# 3.1. .reverse() / reversed() 뒤집기
# int_prices.reverse() #=> [10, 3, 2]

# 3.2. sorted() + reversed()
# sorted_prices = reversed(sorted(int_prices)) #=> [10, 3, 2]
# or sorted_prices = sorted(int_prices, reverse=True)

# 3.3.
sorted_prices = sorted(list( map(int, prices)),reverse=True)
# 4. 출력
for i in sorted_prices:
    print(i)