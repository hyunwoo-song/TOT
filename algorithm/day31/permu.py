N= 3
A = [1,2,3]
Visited=[0]*N

def Per(num):
    Visited[num] =A[num]
    for i in range(N):
        if not Visited[i]:
            Per(i)
            Visited[i] =0

for j in range(N):
    Per(j)
    Visited[j] = 0

