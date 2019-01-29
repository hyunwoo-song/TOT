T = int(input())
for _ in range(T):
    N = int(input())
    l = [0]*N
    sum_N =0
    for i in range(1,N+1):
        l[i-1] = i
    for j in l:
        if j % 2:
            sum_N += j
        else:
            sum_N -= j

    print(f'#{_+1} {sum_N}')