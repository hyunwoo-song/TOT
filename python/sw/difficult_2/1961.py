T =int(input())
for t in range(T):
    N = int(input())
    l = [0]*N
    for n in range(N):
        l[n] = list(map(int, input().split()))
        