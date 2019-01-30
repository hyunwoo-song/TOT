S = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
l = [0]*8
for t in range(T):
    price = int(input())
    for i in range(8):
        l[i] = str(price // S[i])
        price = price - S[i]*int(l[i])
    print(f'#{t+1}')
    print(' '.join(l))