import sys
sys.stdin = open('love.txt')
from collections import deque

Que = deque()

def COMBI(num):
    global N
    Visited[num] = 1
    Que.append(Arr[num])

    if len(Que) == 2:
        t1= Que.popleft()
        y1 = t1[0]
        x1 = t1[1]

        t2 = Que.popleft()
        y2 = t2[0]
        x2 = t2[1]

        y= y2-y1
        x= x2-x1

        Result.append((y,x))


    for i in range(N):
        if not Visited[i]:
            COMBI(i)
            Visited[i] = 0


TC= int(input())
for tc in range(1, TC+1):
    N = int(input())
    Arr=[list(map(int, input().split())) for n in range(N)]
    print(Arr)
    Result = []
    Visited=[0]*N
    COMBI(0)



