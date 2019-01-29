T=int(input())
for _ in range(T):
    N, M= map(int, input().split())
    l = [0]*N
    max_l = 0
    sum_l = 0
    for n in range(N):
        l[n] = list(map(int, input().split()))
    for j in range(M):
        sum_l = 0
        for i in range(M+1):
            if M+j <= N:
                if i+j <= N:
                    sum_l += sum(l[i+j][j:M+j])
        if sum_l >= max_l:
            max_l = sum_l
    
    print(f'#{_+1} {max_l}')