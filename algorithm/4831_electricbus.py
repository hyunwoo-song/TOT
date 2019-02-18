import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    s = list(map(int, input().split()))
    count = 0
    m = K
    for i in range(N):
        if m in s:
            count += 1
            m += K
        else:
            m -= 1
        if m == N:
            break
    if m < N:
        count = 0

    print(f'#{t} {count}')
