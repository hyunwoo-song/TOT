T= int(input())
count =0
l = []
for i in range(1,T+1):
    if not T % i: 
        print(f'{i}(은)는 {T}의 약수 입니다.')
        count += 1
        l += [i]
if count == 2:
    print(f'{T}(은)는 {l[0]}과 {l[1]}로만 나눌 수 있는 소수입니다.')
