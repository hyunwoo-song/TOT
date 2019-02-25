import sys
sys.stdin = open('input.txt', 'r')




def S(y):
    global N, sum_S, bin, msum_S

    if msum_S < sum_S:
        return

    if y == N:
        if msum_S >= sum_S:
            msum_S = sum_S
        bin.append(msum_S)

    if y >= N:
        return

    for dx in range(N):
        if not visited_x[dx]:
            visited_x[dx] = True
            sum_S += Arr[y][dx]
            S(y + 1)

            visited_x[dx] = False
            sum_S -= Arr[y][dx]


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    visited_x = [0] * N
    Arr = []
    sum_S = 0
    y = 0
    bin=[]
    msum_S = 0x7FFFFFFF
    for n in range(N):
        Arr.append(list(map(int, input().split())))
    S(0)
    print(f'#{t} {msum_S}')