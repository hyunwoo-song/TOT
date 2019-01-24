N = int(input())
for i in range(2,N):
    if not N % i :
        result = "소수가 아닙니다."
    else:
        result ='소수입니다.'


print(result)