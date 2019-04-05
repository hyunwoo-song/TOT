import sys
sys.stdin=open('5644.txt')

def GO(ta, tb):
    global result










def ISSAFE(y2,x2,y1,x1,c):
    if 0<= y2 <10 and 0<= x2 <10:
        if c >= abs(y2-y1) +abs(x2 - x1):
            return True


def CHECK(x, y, c, p,y1,x1):
    Map[y][x]= p
    for dir in range(4):
        Y = y+ Dy[dir]
        X = x+ Dx[dir]

        if ISSAFE(Y,X,y1,x1,c):
            if Map[Y][X] < p:
                CHECK(X, Y, c, p,y1,x1)


Dy=[0,-1,0,1,0]
Dx=[0,0,1,0,-1]


TC = int(input())
for tc in range(1, TC+1):
    Time, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Map=[[0]*10 for _ in range(10)]
    for n in range(N):
        x, y, c, p = map(int, input().split())
        x1= x-1
        y1= y-1
        CHECK(x-1, y-1, c, p,y1,x1)

    result = 
    for t in range(Time):
        GO(A[t], B[t])