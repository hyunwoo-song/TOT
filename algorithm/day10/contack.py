import sys
sys.stdin =open('input.txt', 'r')

def F_D(Distance):
    M_D = 0
    M_D_i = 0
    for i in range(len(Distance)):
        if M_D <= Distance[i]:
            M_D = Distance[i]
            M_D_i = i
    return M_D_i

def visit(t):
    for l in range(1, Length):
        if Mymap[t][l] and not Visited[l]:
                Que.append(l)
                Visited[l] = True
                Distance[l] = Distance[t] + 1

def BFS(Start):
    Que.append(Start)
    Visited[Start] = True
    while Que:
        t = Que.pop(0)
        visit(t)


T = 10
for t in range(1,T+1):
    Length, Start = map(int, input().split())
    Bisang = list(map(int, input().split()))
    Mymap = [[0]*(Length+1) for _ in range((Length+1))]
    Visited = [0]*(Length+1)
    Distance = [0]*(Length +1)
    Que = []

    for b in range(0,len(Bisang),2):
        Mymap[Bisang[b]][Bisang[b+1]] = True

    BFS(Start)

    print(f'#{t} {F_D(Distance)}')


