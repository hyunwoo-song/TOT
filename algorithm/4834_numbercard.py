import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ai=list(map(int, input()))

    counting=[0]*10
    max_c = 0
    card = 0
    for i in ai:
        counting[i] += 1
        max_c = max(counting)
    for j in range(len(counting)):
        if max_c == counting[j]:
            card = j

    print(f'#{t} {card} {max_c}')