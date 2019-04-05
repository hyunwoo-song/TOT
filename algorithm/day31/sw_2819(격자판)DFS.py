import sys
sys.stdin = open('2819.txt')


def ISSAFE(a,b):
    if 0<= a < 4 and 0 <= b < 4:
        return True


def DFS(y,x):
    global S, cnt
    S += Arr[y][x]
    cnt += 1

    if cnt == 7:
        if not S in Result:
            Result.append(S)
            return
        else:
            return

    for dir in range(4):
        Y = y + Dy[dir]
        X = x + Dx[dir]

        if ISSAFE(Y, X):
            DFS(Y,X)
            cnt -= 1
            S= S[:-1]

Dy=[0,0,1,-1]
Dx=[1,-1,0,0]

TC = int(input())
for tc in range(1, TC+1):
    Arr = [list(map(str, input().split())) for n in range(4)]
    Result=[]

    for y in range(4):
        for x in range(4):
            cnt = 0
            S = ''
            DFS(y,x)
    print('#{} {}'.format(tc , len(Result)))