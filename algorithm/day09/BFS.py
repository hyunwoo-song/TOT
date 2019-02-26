import sys
sys.stdin= open('input.txt', 'r')


def visit(t):
    for i in range(1, N + 1):
        if Mymap[t][i] and not visited[i]:
            if not i in Que:
                Que.append(i)
                Distance[i] = Distance[t] + 1
                Parent[i] = t


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

