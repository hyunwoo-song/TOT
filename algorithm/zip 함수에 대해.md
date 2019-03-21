##### 파이썬에서는

파이썬의 sorted를 사용해보세요. 반복문이나, deepcopy 함수를 사용하지 않아도 새로운 정렬된 리스트를 구할 수 있습니다.

```python
list1 = [3, 2, 1]
list2 = sorted(list1)
```



##### 파이썬에서는

파이썬은 이런 데이터를 상수(constants)로 정의해놓았습니다.

```ptyhon
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
```



##### 파이썬에서는

파이썬에서는 [ljust](https://docs.python.org/3/library/stdtypes.html?highlight=rjust#str.ljust), [center](https://docs.python.org/3/library/stdtypes.html?highlight=rjust#str.center), [rjust](https://docs.python.org/3/library/stdtypes.html?highlight=rjust#str.rjust)와 같은 string의 메소드를 사용해 코드를 획기적으로 줄일 수 있습니다.

```python
s = 'abc'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬
```



##### 파이썬에서는

파이썬의 [int(x, base = 10)](https://docs.python.org/3/library/functions.html#int) 함수는 진법 변환을 지원합니다.
이 기본적인 함수를 잘 쓰면 코드를 짧게 쓸 수 있고, 또 시간을 절약할 수 있습니다.

```
num = '3212'
base = 5
answer = int(num, base)
```



##### python에서는

파이썬의 [zip](https://docs.python.org/3/library/functions.html?highlight=built%20function#zip)과 unpacking 을 이용하면 코드 한 줄로 리스트를 뒤집을 수 있습니다.

```
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))
new_list = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```



### zip 함수에 대해

[파이썬 3 한글 번역 - zip](https://docs.python.org/ko/3/library/functions.html?highlight=built%20function)에 따르면

> zip(*iterables)는 각 iterables 의 요소들을 모으는 이터레이터를 만듭니다. 
> 튜플의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.

영어 원문:

> Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

```
mylist = [ 1,2,3 ]
new_list = [ 40, 50, 60 ]
for i in zip(mylist, new_list):
    print (i)

(1, 40)
(2, 50)
(3, 60)
```

##### 사용 예 #1 - 여러 개의 Iterable 동시에 순회할 때 사용

```
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for i, j, k in zip(list1, list2, list3):
   print( i + j + k )
```

##### 사용 예 #2 - Key 리스트와 Value 리스트로 딕셔너리 생성하기

파이썬의 zip 함수와 dict 생성자를 이용하면 **코드 단 한 줄**로, 두 리스트를 합쳐 딕셔너리로 만들 수 있습니다.

```
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```



##### 파이썬에서는

파이썬의 `map`을 사용하면 for 문을 사용하지 않고도 멤버의 타입을 일괄 변환할 수 있습니다.

```python
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
```





```
def solution(mylist):
    answer = list((, mylist))
    return answer
```





##### 파이썬에서는

파이썬의 join을 사용하면 이 코드를 두 줄로 줄일 수 있습니다 .

```python
my_list = ['1', '100', '33']
answer = ''.join(my_list)
```



##### 파이썬에서는

파이썬에서는 `*`연산자를 사용해 코드를 획기적으로 줄일 수 있습니다.

```python
n = 어쩌고
answer = 'abc'*n
```

또, `*` 연산자를 이용하면 [123, 456, 123, 456, 123 ...] 과같이 123, 456이 n번 반복되는 리스트를 만들 수 있습니다.

```python
n = 어쩌고
answer= [123, 456]*n
```



##### 파이썬에서는 곱집합(Cartesian product) 구하기 - product

[itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product)를 이용하면, for 문을 사용하지 않고도 곱집합을 구할 수 있습니다.

```python
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
itertools.product(iterable1, iterable2, iterable3)
```



##### 파이썬에서는

파이썬의 다양한 기능을 사용하면, for 문을 사용하지 않고도 리스트를 이어붙일 수 있습니다.

```python
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용2
from functools import reduce
import operator
list(reduce(operator.add, my_list))


[1, 2, 3, 4, 5, 6]
```



##### 파이썬에서는

[itertools.permutation](https://docs.python.org/3/library/itertools.html#itertools.permutations)를 이용하면, for문을 사용하지 않고도 순열을 구할 수 있습니다.

```python
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
```



##### 파이썬에서는

파이썬의 collection.Counter 클래스를 사용하면 이 코드를 간략하게 만들 수 있습니다.

```python
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0
```



##### 파이썬에서는

파이썬의 list comprehension을 사용하면 한 줄 안에 for 문과 if 문을 한 번에 처리할 수 있습니다.

```python
mylist = [3, 2, 6, 7]
answer = [ i**2 for i in mylist if i %2 == 0]
```

list comprehension의 syntax는 [Displays for lists, sets and dictionaries](https://docs.python.org/3/reference/expressions.html?highlight=list%20comprehension#displays-for-lists-sets-and-dictionaries) 에서 확인하실 수 있습니다. [1](https://programmers.co.kr/learn/courses/4008/lessons/48464#fn1)



##### 파이썬에서는

파이썬의 [bisect.bisect](https://docs.python.org/3.6/library/bisect.html#bisect.bisect) 메소드를 사용하면 이 코드를 간략하게 만들 수 있습니다.

```python
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
```