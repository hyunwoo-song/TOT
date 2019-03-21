import sys
sys.stdin = open('5188.txt', 'r')

def ISSAFE(a,b):
    global N
    if 0<= a and a <N and 0 <= b and b <N:
        if not Visited[a][b]:
            return True


def DFS(y,x):
    global sum_Arr
    Visited[y][x]= True
    sum_Arr += Arr[y][x]


    for dir in range(2):
        new_y = y+ Dy[dir]
        new_x = x+ Dx[dir]

        if ISSAFE(new_y, new_x):
            DFS(new_y,new_x)
            if new_y == N-1 and new_x == N-1:
                Sum.append(sum_Arr)
            sum_Arr -= Arr[new_y][new_x]
            Visited[new_y][new_x] = False



Dy=[1,0]
Dx=[0,1]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    Arr = [list(map(int,input().split())) for n in range(N)]
    Visited = [[0]*N for n in range(N)]
    sum_Arr = 0
    Sum = []
    DFS(0,0)

    print('#{} {}'.format(t, min(Sum)))
