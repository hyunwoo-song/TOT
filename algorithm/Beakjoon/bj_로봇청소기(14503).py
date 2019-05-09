import sys
sys.stdin = open('robot.txt')

def ISSAFE(y,x):
    if 0<y<N and 0<x<N:
        return True

def CLEAN(y,x,dir):
    global cnt, flag, fflag

    if A[y][x] == 0:
        A[y][x]= 2
        cnt += 1

    flag = 1

    if fflag:
        return

    for i in range(dir+3,dir-1,-1):
        i %= 4
        Y = y + Dy[i]
        X = x + Dx[i]
        if ISSAFE(Y,X):
            if A[Y][X] ==0:
                A[Y][X] = 2
                cnt +=1
                CLEAN(Y, X, i)
                flag = 0
                break

    if flag:
        Y = y-Dy[i]
        X = x-Dx[i]

        if ISSAFE(Y,X):
            if A[Y][X] != 1:
                CLEAN(Y,X,i)
            else:
                return
        else:
            fflag = 1
            return

Dy=[-1,0,1,0]
Dx=[0,1,0,-1]
N, M = map(int, input().split())
r, c, d = map(int,input().split())
A= [list(map(int, input().split())) for n in range(N)]

cnt = 0
flag = 1
fflag= 0
CLEAN(r,c,d)
print(cnt)