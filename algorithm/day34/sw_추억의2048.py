import sys
sys.stdin = open('2048.txt')
def DDD(dir):
    global cnt
    if D == 'right':
        return
    elif D == 'up':
        cnt = 1
    elif D == 'left':
        cnt = 2
    else:
        cnt = 3
    return

def Turn(L):
    for y in range(N):
        for x in range(N):
            temp[x][N-y-1] = L[y][x]
    for i in range(N):
        L[i] = temp[i][:]

TC = int(input())
for tc in range(1, TC+1):
    N, D = map(str, input().split())
    N= int(N)
    Arr= []
    temp = [[0] * N for n in range(N)]
    Result = [[0] * N for n in range(N)]
    Game= [list(map(int, input().split())) for n in range(N)]

    cnt = 0
    DDD(D)
    for c in range(cnt):
        Turn(Game)

    for n in range(N):
        A = []
        for g in range(len(Game[n])-1,-1,-1):
            if Game[n][g]:
                A.append(Game[n][g])
        if A:
            B=[A[0]]
            flag = 0
            for a in range(1, len(A)):
                if flag:
                    B.append(A[a])
                    flag=0
                    continue

                if A[a] == B[-1]:
                    B[-1] += A[a]
                    flag = 1
                    continue

                else:
                    B.append(A[a])

            c= N-1
            while B:
                b = B.pop(0)
                Result[n][c] = b
                c -= 1

    for c in range(4-cnt):
        Turn(Result)

    print('#{}'.format(tc))
    for n in range(N):
        print(*Result[n])









