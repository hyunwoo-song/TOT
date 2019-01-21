T = int(input())

for i in range(1,T+1):
    if not T % i:
        print(f'{i}(은)는 {T}의 약수입니다.')