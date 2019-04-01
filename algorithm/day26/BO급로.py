import sys
sys.stdin = open('bo.txt')


def ISSAFE(a,b):
    if 0<= a and a < N and 0 <= b and b < N:
        return True


def Go(y,x):
    global k, result

    if y==x==N-1:
        if result > Visited[y][x]:
            result = Visited[y][x]
            return

    for dir in range(4):
        Y = y + Dy[dir]
        X = x + Dx[dir]

        if ISSAFE(Y,X):
            if Visited[y][x] + Arr[Y][X] < result:
                if Visited[Y][X] == -1:
                    Visited[Y][X] = Visited[y][x] + Arr[Y][X]
                    Go(Y, X)

                else:
                    if Visited[y][x] + Arr[Y][X] < Visited[Y][X]:
                        Visited[Y][X] = Visited[y][x] + Arr[Y][X]
                        Go(Y, X)


Dy=[0,1,-1,0]
Dx=[1,0,0,-1]

TC= int(input())
for tc in range(1,TC+1):
    N= int(input())
    Arr = [list(map(int, input())) for n in range(N)]
    Visited=[[-1]*N for n in range(N)]
    Visited[0][0]=0
    result =0x7FFFFFFF
    Go(0,0)

    print('#{} {}' .format(tc, result))