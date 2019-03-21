import sys
sys.stdin = open('input.txt')

import itertools


def back(cnt):
    global result,N, rrr, RRR
    if cnt == N:
        for qq in range(len(result)):
            w = 0
            while w < N:
                rrr *= P[w][result[qq]] / 100
                w += 1

            if RRR < rrr:
                RRR = rrr * 100
            rrr = 1
        print('#%d %.6f' % (t, RRR))

        return


    for i in range(len(data)):
        if not visited[i]:
            visited[i] = 1
            result[cnt] = data[i]
            if cnt +1 <= N:
                back(cnt + 1)
                result[cnt] = 0
                visited[i] = 0


T = int(input())
for t in range(1,T+1):
    N = int(input())
    P=[]
    rrr = 1
    RRR =0

    data = [j for j in range(N)]
    visited = [0] * len(data)
    result = [0] * len(data)
    back(0)

    for n in range(N):
        P.append(list(map(int, input().split())))





