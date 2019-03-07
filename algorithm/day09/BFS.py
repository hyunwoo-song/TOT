import sys
sys.stdin= open('input.txt', 'r')


def visit(new_y, new_x):
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


def BFS(here):
    Que.append(here)
    Distance[here] = 0
    while Que:
        t = Que.pop(0)
        if not visited[t]:
            print(t)
            visited[t] = True
        visit(t)

N = 7
Parent = [0] * (N + 1)
Distance = [0] * (N + 1)
visited = [0] * (N + 1)
result = 0
Que = []
L = list(map(int, (input().split())))
print(L)

Mymap = [[0] * (N + 1) for _ in range(N + 1)]
for l in range(0, len(L), 2):
    Mymap[L[l]][L[l + 1]] = True

BFS(1)
print(Distance, Parent)

