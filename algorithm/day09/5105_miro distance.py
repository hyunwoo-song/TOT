import sys
sys.stdin = open('input.txt', 'r')

def visit(y, x):
    global D_result
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y and new_y <= N - 1 and new_x <= N - 1 and 0 <= new_x:
            if Miro[new_y][new_x] != 1 and not visited[new_y][new_x]:
                if not [new_y, new_x] in Que:
                    Que.append([new_y, new_x])
                    Distance[new_y][new_x] = Distance[y][x] + 1

                if Miro[new_y][new_x] == 3:
                    D_result = Distance[new_y][new_x] -1
                    return D_result

def BFS(y,x):
    Que.append([y, x])
    Distance[y][x] = 0
    while Que:
        T = Que.pop(0)
        y = T[0]
        x = T[1]

        if not visited[y][x]:
            visited[y][x] = True
        visit(y, x)


dy=[0,0,-1,1]
dx=[-1,1,0,0]
T = int(input())

for t in range(1, T+1):
    N = int(input())
    Miro=[]
    result = 0
    Distance=[[0]*(N) for _ in range(N)]
    Que = []
    visited = [[0] * (N) for _ in range(N)]
    D_result =0

    for n in range(N):
        Miro.append(list(map(int, input())))

    for _ in range(N):
        for __ in range(N):
            if Miro[_][__] == 2:
                x=__
                y=_

    BFS(y,x)
    print(f'#{t} {D_result}')
