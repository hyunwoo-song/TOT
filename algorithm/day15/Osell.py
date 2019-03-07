import sys
sys.stdin = open ('input.txt', 'r')


def king(dy,dx,new_y,new_x,k,doll):
    global count
    Map[new_y][new_x] = doll
    new_y += dy
    new_x += dx
    count +=1

    if not Map[new_y][new_x]:
        while count != 0:
            count -=1
            new_y -= dy
            new_x -= dx
            Map[new_y][new_x]= k
        return

    elif Map[new_y][new_x]==doll:
        count = 0
        return

    else:
        king(dy, dx, new_y, new_x, k, doll)


def Find(y,x,doll):
    global N,k

    if doll == 1:
        k =2
    elif doll == 2:
        k = 1

    for dir in range(8):
        dy=Y[dir]
        dx=X[dir]
        new_y = y+ dy
        new_x = x+ dx
        if 0< new_y and new_y < N+1 and 0< new_x and new_x < N+1:
            if Map[new_y][new_x] and Map[new_y][new_x] != doll:
                king(dy,dx,new_y,new_x,k,doll)
    return


Y= [-1,-1,-1,0,0,1,1,1]
X=[-1,0,1,-1,1,-1,0,1]


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Map = [[0]*(N+2) for n in range(N+2)]

    Map[N//2][N//2]=2
    Map[(N // 2)+1][N // 2] = 1
    Map[N // 2 ][(N // 2)+1] = 1
    Map[(N // 2) + 1][(N // 2)+1] = 2
    k=0
    count = 0
    for m in range(M):
        x, y, doll=map(int, input().split())
        Map[y][x] = doll
        Find(y, x, doll)
        count = 0

    result_A =0
    result_B = 0

    for i in range(N+2):
        for j in range(N+2):
            if Map[i][j] == 1:
                result_A += 1
            elif Map[i][j] == 2:
                result_B += 1

    print('#{} {} {}'.format(t, result_A, result_B))





