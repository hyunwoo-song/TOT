# # 1. Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요.
# import keyword
# print(keyword.kwlist)



# # 2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다.
# # (floating point rounding error)
# # 따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.
# a = 0.1 * 3
# b = 0.3

# import math
# math.isclose(a,b)

# # 3. 이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) \ 을 작성하세요.
# print('hi\nhello\t\\')


# 4. “안녕, 철수야”를 String Interpolation을 사용하여 출력하세요 3가지 방법
# name = "철수"
# print(f'"안녕, {name}야"')
# print('"안녕, %s야"' %name)
# print('"안녕, {}야"'.format(name))


# 5. 다음 중 형변환시 오류가 발생하는 것은?
# str(1)
# int(‘30’)
# int(5)
# bool(‘50’)
# int(‘3.5’)   -> float('3.5')



# 5. 변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을 분류하시오.
# String, List, Tuple, Range, Set, Dictionary

# list set dictionary 변경가능


