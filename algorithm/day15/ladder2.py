import sys
sys.stdin = open('input.txt', 'r')

def visit(y, x):
    for dir in range(3):
        new_y = y + dy[dir]
        new_x = x + dx[dir]

        if 0 <= new_y and new_y <= 9 and new_x <= 9 and 0 <= new_x:
            if Data[new_y][new_x] == 1 and not Visited[new_y][new_x]:
                if not [new_y, new_x] in Que:
                    Que.append([new_y, new_x])
                    Distance[new_y][new_x] = Distance[y][x] + 1

                    return



def BFS(Y,X):
    if X == 0:
        for i in range(10):
            if Data[Y][i]:
                Que.append([Y,i])

    Distance[Y][X] = 0

    while Que:
        t = Que.pop(0)
        y=t[0]
        x=t[1]
        if not Visited[y][x]:
            Visited[y][x] = True
        visit(y, x)


dy=[0,0,1]
dx=[-1,1,0]

T = 1
for t in range(1, T+1):
    N= int(input())
    Data=[list(map(int, input().split())) for _ in range(10)]
    Que=[]
    Distance=[[0]*10 for _ in range(10)]
    Visited = [[0] * 10 for _ in range(10)]
    BFS(0,0)