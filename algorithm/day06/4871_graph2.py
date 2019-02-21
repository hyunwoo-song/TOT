import sys
sys.stdin = open('input.txt', 'r')

def DFS(here):
    global result
    visited[here] = True

    for next in range(V+1):
        if MyMap[here][next] and not visited[next]:
            DFS(next)

    if visited[G]:
        result =1
        return result

    else:
        return result





T =int(input())
for t in range(1, T+1):
    V, E = map(int, (input().split()))
    L = []
    result = 0

    for e in range(E):
        L.append(list(map(int, input().split())))
    S, G = map(int, input().split())

    MyMap = [[0]*(V+1) for v in range(V+1)]
    visited = [0]*(V+1)
    print(L)
    for l in range(len(L)):
        y= L[l][0]
        x=L[l][1]
        MyMap[y][x]= True
    print(MyMap)
    print(f'#{t} {DFS(S)}')