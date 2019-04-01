import sys
sys.stdin = open('ex4.txt')

N, M = map(int, input().split())
Mymap=[[0x7FFFFFFF]*N for n in range(N)]
T=[]
Dis=[]
for m in range(M):
    S, E, V = map(int,input().split())
    Mymap[S][E] = V

for n in range(N):
    T.append(n)
    Dis.append(Mymap[0][n])
    Mymap[n][n]= 0
T.pop(0)


while T:
    z = 0x7FFFFFFF
    for t in range(len(T)):
        if z >= Dis[T[t]]:
            z = Dis[T[t]]
            v = T[t]
            k=t
    T.pop(k)

    for w in T:
        Dis[w] = min(Dis[w], Dis[v]+ Mymap[v][w])

print(Dis)