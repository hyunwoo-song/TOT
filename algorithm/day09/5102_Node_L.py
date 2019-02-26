import sys
sys.stdin = open('input.txt', 'r')


def visit(here):
    for next in range(1, V + 1):
        if Mymap[here][next] and not visited[next]:
            if not next in Que:
                Que.append(next)
                Distance[next] = Distance[here] + 1

def BFS(here):
    Que.append(here)
    Distance[here] = 0
    while Que:
        here = Que.pop(0)
        if not visited[here]:
            visited[here] = True
        visit(here)



T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    Mymap = [[0]*(V+1) for v in range(V+1)]
    visited=[0]*(V+1)
    L=[]
    Distance=[0]*(V+1)
    Que=[]

    for e in range(E):
        L.append(list(map(int, input().split())))
        Mymap[L[e][0]][L[e][1]] = True
        Mymap[L[e][1]][L[e][0]] = True
    S, G = map(int, input().split())

    BFS(S)
    print(f'#{t} {Distance[G]}')


