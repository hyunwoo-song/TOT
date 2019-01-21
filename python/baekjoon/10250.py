T = int(input())
for n in range(T):
    H, W, N = map(int, input().split())
    Mok = N//H 
    Na = N % H
    l= [0,0,0]
    s = ''
    count = Mok +1
    if not Na:
        Na = H
        count = Mok 
    l[0] += Na

    if count >= 10:
        s += str(count)
        for j in range(len(s)): 
            l[j+1] = s[j]
    else:
        l[2] = count
    print(f'{str(l[0])+str(l[1])+str(l[2])}')
