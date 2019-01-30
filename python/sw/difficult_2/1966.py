T = int(input())

for t in range(T):
    s=[]
    N = int(input())
    l = list(map(int, input().split()))
    sorted_l = sorted(l)
    for i in sorted_l:
        s.append(str(i))
    k = ' '.join(s)
    print(f'#{t+1} {k}')



