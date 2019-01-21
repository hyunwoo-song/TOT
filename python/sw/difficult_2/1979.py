# T = int(input())
# for n in range(T):
    N,K =map(int,input().split())
    count = 0
    D = {}
    for i in range(N):
        a = list(map(int,input().split()))
        b = a.count(1)
        D.update({i: a})
        if b == K:
            count += 1
    print(count)
    print(D)
        for j in range(N):
            print(D[j][j])
