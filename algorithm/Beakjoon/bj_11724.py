import sys
sys.stdin = open('11724.txt', 'r')

def Go(num):
    global count
    if Visited[num]:
        count += 1
        return

    else:
        Visited[num] = True
        for i in range(1, N+1):
            if Mymap[num][i]:
                R.append(i)
                Go(i)



N, M = map(int, input().split())
Mymap=[[0]*(N+1) for n in range(N+1)]
Visited=[0]*(N+1)
count = 1
R=[]
for m in range(M):
    u, v = map(int, input().split())
    Mymap[u][v] = True

Go(1)
print(count)