# 다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.

T = int(input())
l= []
mok = T // 2
while mok != 0 :
    na = str(T % 2)
    l += [na]
    T = mok
    mok = T // 2
l +=[na]
z=l[::-1]
print(''.join(z))
