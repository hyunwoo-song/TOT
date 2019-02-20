import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

T = int(input())
Arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(Arr)
# n=5
# i  =  0 00000 ~ 0 11111
# j =   00000
#       00001
#       00010
#       00100
#       01000
#       10000
for t in range(1,T+1):
    N, K = map(int,input().split())
    count=0
    for i in range(1<<n):
        bin = []
        for j in range(n):
            if i & (1<<j):
                bin.append(Arr[j])

        if sum(bin) == K:
           if len(bin) == N:
                 count += 1

    print(f'#{t} {count}')









