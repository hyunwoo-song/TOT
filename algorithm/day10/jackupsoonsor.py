import sys
sys.stdin = open('input.txt', 'r')

def visit(t):
    Visited[t] = True
    Result.append(t)
    for v in range(V+1):
        if Mymap[t][v] and not Visited[v]:
            if Count[v] == 1:
                Que.append(v)
                Count[v] -= 1
            else:
                Count[v] -= 1
    return






def BFS(Que):
    while Que:
        t = Que.pop(0)
        visit(t)
    return

T = 1
for t in range(1, T+1):
    V, E = map(int, input().split())
    L = list(map(int, input().split()))


    Start=[i for i in range(1,(V+1))]
    Start2 = []
    Que= []
    Mymap = [[0]*(V+1) for v in range(V+1)]
    Visited = [0]*(V+1)
    Result=[]
    Count =[0]* (V+1)

    for l in range(0,len(L),2):
        Mymap[L[l]][L[l+1]]= True
        Start2.append(L[l+1])
        Count[L[l+1]] += 1

    for s in Start:
        if not s in Start2:
            Que.append(s)

    BFS(Que)
    print(f'#{t} {" ".join(map(str, Result))}')