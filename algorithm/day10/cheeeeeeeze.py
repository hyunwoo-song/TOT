import sys
sys.stdin = open('input.txt', 'r')


def visit(new_y, new_x):
    for i in range(4):
        new_y += dy[i]
        new_x += dx[i]
        if 0 <= new_y and new_y <= N - 1 and new_x <= M - 1 and 0 <= new_x:
            if not Tong[new_y][new_x] and not Visited[new_y][new_x]:
                    Que.append([new_y, new_x])
                    Visited[new_y][new_x] = True
            elif Tong[new_y][new_x]==1:
                Tong[new_y][new_x] = -1


def BFS(y,x):
    global count, Time
    count = 0
    Que.append([y,x])
    Visited[y][x] = True
    while Que:
        t = Que.pop(0)
        new_y=t[0]
        new_x=t[1]
        visit(new_y, new_x)
    for i in range(N):
        for j in range(M):
            if Tong[i][j] == -1:
                Tong[i][j] = 0
                Time += 1
                count += 1
                Count.append(count)
    return Time

N, M = map(int, input().split())
Tong = []
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]
Visited = [[0] * N for _ in range(N)]
Que = []
Count = [1]
Time =0
for n in range(N):
    Tong.append(list(map(int, input().split())))


while Count[-1] > 0:
    print(Count, BFS(0, 0))
