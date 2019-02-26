import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    M = M % N
    for m in range(M):
        L.append(L.pop(0))
    print(f'#{t} {L.pop(0)}')