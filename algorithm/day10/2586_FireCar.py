import sys
sys.stdin=open('input.txt', 'r')

def visit(t):
    Go =[-1,1]
    D = 0
    for go in Go:
        while Line[t+go] != 3:
            t += go
        if Line[t] == 3:
            Line[t]=0
            D += t
    return Distance.append(D)

def BFS(Start):
    Que.append(Start)
    while Que:
        t = Que.pop(0)
        visit(t)



def Point(list, n):
    for l in list:
        Line[l] = n

P, F = map(int, input().split())
P_point = list(map(int, input().split()))
F_point = list(map(int, input().split()))

Line = [0]* 100001
Point(P_point, 3)
Point(F_point, 2)


Distance = []
Que = []
for f in F_point:
    BFS(f)
print(Distance)