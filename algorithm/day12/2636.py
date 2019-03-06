import sys
sys.stdin = open('input.txt', 'r')

def visit(new_y,new_x):
    if Mymap[new_y][new_x] and not visited[new_y][new_y]:
        if not i in Que:
            Que.append(i)
            Distance[i] = Distance[t] + 1
            Parent[i] = t


def BFS(y,x):
    Que.append([y,x])
    while Que:
        t = Que.pop(0)
        new_y=t[0]
        new_x=t[1]

        if not visited[new_y][new_y]:
            visited[new_y][new_y] = True
        visit(new_y,new_x)


N, M = map(int, input().split())
Cz = []
for n in range(N):
    Cz.append(list(map(int, input().split())))

Mymap = [[0] * (N) for _ in range(N)]
visited = [[0] * (N) for n in range(N)]
Que = []
time = 0
count = 0

BFS(0, 0)

