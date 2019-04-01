import sys
sys.stdin = open('5250.txt')

def ISSAFE(a,b):
    if 0<= a < N and 0 <= b < N:
        return True

def VISIT(y,x):
    for dir in range(4):
        Y = y + Dy[dir]
        X = x + Dx[dir]
        if X == 0 and Y == 0:
            continue
        if ISSAFE(Y, X):
            result = 0
            if Arr[Y][X] - Arr[y][x] > 0:
                result = Arr[Y][X] - Arr[y][x]

            if not Visited[Y][X]:
                Visited[Y][X] = Visited[y][x] + result+1
                Que.append([Y, X])
            else:
                if Visited[Y][X] > Visited[y][x] + result+1:
                    Visited[Y][X] = Visited[y][x] + result+1
                    Que.append([Y, X])

def GO(y,x):
    Que.append([y,x])
    while Que:
        t = Que.pop(0)
        y= t[0]
        x= t[1]

        VISIT(y,x)

Dy=[1,0,-1,0]
Dx=[0,1,0,-1]
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Que= []
    Visited=[[0]*N for n in range(N)]
    Arr=[list(map(int,input().split())) for n in range(N)]
    GO(0,0)

    print('#{} {}'.format(tc,Visited[N-1][N-1]))