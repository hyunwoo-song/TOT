import sys
sys.stdin = open('1260.txt', 'r')

def DFS(a):
    Result_D.append(a)
    Visited[a] = True
    for i in range(N+1):
        if Mymap[a][i] and not Visited[i]:
            DFS(i)
    return

def Visit(next):
    Visited[next] =True
    Result_B.append(next)
    for j in range(N+1):
        if Mymap[next][j] and not Visited[j]:
            if not j in Que:
                Que.append(j)

def BFS(here):
    Que.append(here)

    while Que:
        t= Que.pop(0)
        Visit(t)

N, M, V = map(int, input().split())
Visited=[0]*(N+1)
Mymap = [[0]*(N+1) for n in range(N+1)]
Que=[]
Result_D=[]
Result_B=[]
for m in range(M):
    start, end = map(int,input().split())
    Mymap[start][end]= True
    Mymap[end][start] = True

DFS(V)
Visited=[0]*(N+1)
BFS(V)

print(' '.join(map(str, Result_D)))
print(' '.join(map(str, Result_B)))