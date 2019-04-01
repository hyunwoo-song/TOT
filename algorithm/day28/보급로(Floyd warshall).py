import sys
sys.stdin = open('Bo.txt')

def ISSAFE(a, b):
    if 0<=a and a < N and 0<= b and b <N:
        return True

def Go(y, x):
    global N,result

    if y == N-1 and x == N-1:
        return

    for dir in range(4):
        Y = y + Dy[dir]
        X = x + Dx[dir]

        if ISSAFE(Y, X):
            if result > Map[Y][X]:
                result = Map[Y][X]

    Arr[Y][X] = Arr[y][x] + Map[Y][X]

Dy=[1,0,-1,0]
Dx=[0,1,0,-1]


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Map = [list(map(int, input())) for n in range(N)]
    Arr= [[0]*N for n in range(N)]
    L = []

    result = 0

    Go(0,0)






