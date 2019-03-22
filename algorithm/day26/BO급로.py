import sys
sys.stdin =  open('Bo.txt')

def ISSAFE(a,b):
    global N
    if 0<=a and a < N and 0 <= b and b < N:
        return True


def Go(y,x):
    global N,result,k
    k += Arr[y][x]
    Visited[y][x] = k
    result += Arr[y][x]

    if y == N-1 and x == N-1:
        Result.append(result)
        return

    for dir in range(4):
        Y = y + Dy[dir]
        X = x + Dx[dir]

        if ISSAFE(Y,X):
            if not Visited[Y][X]:
                Go(Y,X)
                k += Arr[y][x]










Dy=[1,0,-1,0]
Dx=[0,1,0,-1]

TC = int(input())
for tc in range(1, TC+1):
    k=0
    N = int(input())
    Arr=[list(map(int,input())) for n in range(N)]
    Visited= [[0]*N for n in range(N)]
    Mymap=[[0]*N for n in range(N)]
    result = 0
    Result=[]
    Go(0,0)
    print(min(Result))