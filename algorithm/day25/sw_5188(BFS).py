import sys
sys.stdin = open('5188.txt', 'r')

def ISSAFE(a,b):
    global N
    if 0<= a and a <N and 0 <= b and b <N:
        return True


def VISIT(a,b):


    for dir in range(2):
        new_y = a +Dy[dir]
        new_x = b + Dx[dir]
        if ISSAFE(new_y,new_x):
            if Visited[new_y][new_x] > Arr[new_y][new_x] + Visited[a][b]:
                Visited[new_y][new_x] = Arr[new_y][new_x] + Visited[a][b]
                Que.append([new_y, new_x])



def BFS(y,x):
    Que.append([y,x])
    Visited[y][x] = Arr[y][x]

    while Que:
        t = Que.pop(0)
        Y= t[0]
        X= t[1]
        VISIT(Y,X)



Dy=[1,0]
Dx=[0,1]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    Arr = [list(map(int,input().split())) for n in range(N)]
    Visited = [[0x7FFFFFFF]*N for n in range(N)]
    sum_Arr = 0
    Sum = []
    Que=[]
    BFS(0,0)


    print('#{} {}'.format(t, Visited[N-1][N-1]))
