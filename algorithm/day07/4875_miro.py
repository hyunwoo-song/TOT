import sys
sys.stdin = open('input.txt', 'r')

def DFS(y,x):
    global result
    visited[y][x] = True

    for i in range(4):
        new_y = y+ dy[i]
        new_x = x+ dx[i]
        if 0<= new_y and new_y <= N-1 and new_x<=N-1 and 0<= new_x:
            if Miro[new_y][new_x] !=1 and not visited[new_y][new_x]:
                if Miro[new_y][new_x] == 3:
                    result = 1
                    return
                else:
                    DFS(new_y,new_x)

dy=[0,0,-1,1]
dx=[-1,1,0,0]
T = int(input())

for t in range(1, T+1):
    N = int(input())
    Miro=[]
    result = 0
    for n in range(N):
        Miro.append(list(map(int, input())))
    for _ in range(N):
        for __ in range(N):
            if Miro[_][__] == 2:
                X=__
                y=_
                break

    visited= [[0]*N for _ in range(N)]
    DFS(y,X)

    print(f'#{t} {result}')

