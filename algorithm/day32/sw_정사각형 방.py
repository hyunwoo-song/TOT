import sys
sys.stdin = open('tri.txt')

def ISSAFE(a,b):
    global N
    if 0 <= a < N and 0 <= b < N:
        return True

def VISIT(y,x,z,now_dist):
    global result,s,N
    visited[Arr[y][x]]=1
    if z + result > N**2:
        return

    Visited[y][x] = now_dist

    for dir in range(4):
        Y = y + Dy[dir]
        X = x + Dx[dir]

        if ISSAFE(Y,X):
            if Arr[Y][X] - Arr[y][x]== 1:
                if Visited[Y][X] < now_dist + 1:
                    if result < now_dist + 1:
                        result= now_dist + 1
                        s = Arr[Y][X]
                    elif result == now_dist+1:
                        if s > Arr[Y][X]:
                            s= Arr[Y][X]

                    Que.append((Y,X,z,now_dist+1))

def BFS():

    while Que:
        t= Que.popleft()
        y = t[0]
        x = t[1]
        z = t[2]
        now_dist = t[3]
        VISIT(y,x,z,now_dist)

Dy=[1,-1,0,0]
Dx=[0,0,1,-1]

from collections import deque


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Arr=[list(map(int, input().split())) for n in range(N)]
    Visited=[[0]* N for n in range(N)]
    result = 0
    s=0x7FFFFFFF
    visited = [0]*1000000

    for y in range(N):
        for x in range(N):
            if visited[Arr[y][x]]:
                continue
            Que = deque()
            Que.append((y,x,Arr[y][x],0))
            BFS()
    print('#{} {} {}'.format(tc, s-result, result+1))