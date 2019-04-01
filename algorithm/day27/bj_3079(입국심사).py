import sys
sys.stdin = open('3079.txt')




N,M = map(int, input().split())
Time = [int(input()) for n in range(N)]
Time=sorted(Time)
Visitied=[0]*N

start = Time[0]
P=start*(M//2)
k = (M // 2)
result = 0
go = 1
while True:
    P = start * k
    for n in range(N):
        result += P//Time[n]

    if result < M:
        k *= 2
        result = 0
    elif result > M:
        result = 0
        k //=2
    elif result == M:
        result = 0
        print(k)
        break





