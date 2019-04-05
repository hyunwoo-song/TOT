import sys
sys.stdin = open('1953.txt')
from collections import deque
Que=deque()
def ISSAFE(a,b,c,d):
    global N, M
    if 0<=a < N and 0<= b <M and Arr[a][b] != 0:
        if c == 1:
            if d==0:
                if Arr[a][b] in Down:
                    return True
            elif d==1:
                if Arr[a][b] in Up:
                    return True
            elif d==2:
                if Arr[a][b] in Right:
                    return True
            elif d==3:
                if Arr[a][b] in Left:
                    return True

        elif c== 2:
            if d==0:
                if Arr[a][b] in Down:
                    return True
            elif d==1:
                if Arr[a][b] in Up:
                    return True

        elif c==3:
            if d==2:
                if Arr[a][b] in Right:
                    return True
            elif d==3:
                if Arr[a][b] in Left:
                    return True
        elif c==4:
            if d == 1:
                if Arr[a][b] in Up:
                    return True
            elif d==2:
                if Arr[a][b] in Right:
                    return True
        elif c==5:
            if d==0:
                if Arr[a][b] in Down:
                    return True
            elif d==2:
                if Arr[a][b] in Right:
                    return True

        elif c==6:
            if d==0:
                if Arr[a][b] in Down:
                    return True
            elif d==3:
                if Arr[a][b] in Left:
                    return True
        elif c==7:
            if d == 1:
                if Arr[a][b] in Up:
                    return True

            elif d==3:
                if Arr[a][b] in Left:
                    return True

def VISIT(y,x,z):
    global L, cnt
    if z > L:
        return

    Map[y][x] = z
    cnt += 1

    if Arr[y][x] == 1:
        q = Arr[y][x]
        for dir in range(4):
            Y = y + Dy[dir]
            X = x + Dx[dir]

            if ISSAFE(Y, X,q,dir):
                if not Map[Y][X]:
                    Map[Y][X] = z + 1
                    Z = z + 1
                    Que.append([Y, X, Z])
                elif Map[Y][X] > z+1:
                    Map[Y][X] = z+1
                    Z = z+1
                    Que.append([Y,X,Z])


    elif Arr[y][x] == 2:
        q = Arr[y][x]
        for dir in range(2):
            Y = y + Dy[dir]
            X = x + Dx[dir]
            if ISSAFE(Y, X,q,dir):
                if not Map[Y][X]:
                    Map[Y][X] = z + 1
                    Z = z + 1
                    Que.append([Y, X, Z])
                elif Map[Y][X] > z+1:
                    Map[Y][X] = z+1
                    Z = z+1
                    Que.append([Y,X,Z])

    elif Arr[y][x] ==3:
        q = Arr[y][x]
        for dir in range(2,4):
            Y = y + Dy[dir]
            X = x + Dx[dir]
            if ISSAFE(Y, X,q,dir):
                if not Map[Y][X]:
                    Map[Y][X] = z + 1
                    Z = z + 1
                    Que.append([Y, X, Z])
                elif Map[Y][X] > z+1:
                    Map[Y][X] = z+1
                    Z = z+1
                    Que.append([Y,X,Z])

    elif Arr[y][x]==4:
        q = Arr[y][x]
        for dir in range(1,3):
            Y = y + Dy[dir]
            X = x + Dx[dir]
            if ISSAFE(Y, X,q,dir):
                if not Map[Y][X]:
                    Map[Y][X] = z + 1
                    Z = z + 1
                    Que.append([Y, X, Z])
                elif Map[Y][X] > z+1:
                    Map[Y][X] = z+1
                    Z = z+1
                    Que.append([Y,X,Z])

    elif Arr[y][x]==5:
        q = Arr[y][x]
        for dir in range(0,4,2):
            Y = y + Dy[dir]
            X = x + Dx[dir]
            if ISSAFE(Y, X,q,dir):
                if not Map[Y][X]:
                    Map[Y][X] = z + 1
                    Z = z + 1
                    Que.append([Y, X, Z])
                elif Map[Y][X] > z+1:
                    Map[Y][X] = z+1
                    Z = z+1
                    Que.append([Y,X,Z])

    elif Arr[y][x]==6:
        q = Arr[y][x]
        for dir in range(0,4,3):
            Y = y + Dy[dir]
            X = x + Dx[dir]
            if ISSAFE(Y, X,q,dir):
                if not Map[Y][X]:
                    Map[Y][X] = z + 1
                    Z = z + 1
                    Que.append([Y, X, Z])
                elif Map[Y][X] > z+1:
                    Map[Y][X] = z+1
                    Z = z+1
                    Que.append([Y,X,Z])

    elif Arr[y][x]==7:
        q = Arr[y][x]
        for dir in range(1,4,2):
            Y = y + Dy[dir]
            X = x + Dx[dir]
            if ISSAFE(Y, X,q,dir):
                if not Map[Y][X]:
                    Map[Y][X] = z + 1
                    Z = z + 1
                    Que.append([Y, X, Z])
                elif Map[Y][X] > z+1:
                    Map[Y][X] = z+1
                    Z = z+1
                    Que.append([Y,X,Z])

def BFS(y,x,z):

    Que.append([y,x,z])

    while Que:
        t = Que.popleft()
        y=t[0]
        x=t[1]
        z=t[2]

        VISIT(y,x,z)

Down =[1,2,4,7]
Up=[1,2,5,6]
Left=[1,3,4,5]
Right=[1,3,6,7]

Dy=[1,-1,0,0]
Dx=[0,0,1,-1]
TC = int(input())
for tc in range(1,TC+1):
    N, M, R, C, L = map(int,input().split())
    Arr = [list(map(int,input().split())) for n in range(N)]
    Map=[[0]*M for n in range(N)]
    cnt = 0
    BFS(R,C,1)
    print('#{} {}'.format(tc, cnt))