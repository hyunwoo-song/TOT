import sys
sys.stdin = open('5251.txt')

def GO(num):
    global N
    for i in range(N+1):
        Dis[i] = Map[0][i]

    while T:
        w = 0x7FFFFFFF
        for t in range(len(T)):
            if w >= Dis[T[t]]:
                w = Dis[T[t]]
                v = T[t]
                k = t
        T.pop(k)

        for h in T:
            Dis[h] = min(Dis[h], Dis[v]+ Map[v][h])


TC = int(input())
for tc in range(1,TC+1):
    N, E = map(int,input().split())
    Map=[[0x7FFFFFFF]*(N+1) for n in range(N+1)]
    T = [n for n in range(1, N+1)]
    Dis=[0]*(N+1)
    for e in range(E):
        x, y, z = map(int, input().split())
        Map[x][y]= z

    GO(0)
    print('#{} {}'.format(tc, Dis[-1]))