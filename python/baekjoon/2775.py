T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    l_0= []
    l_1= []
    l_2= []
    layer = 0
    for i in range(1,n+1):
        l_0 += [i]
        l_1 += [0*i]
        l_2 += [0*i]
    while layer != k:
        for j_1 in range(n):
            for j_2 in range(j_1+1):
                l_1[j_1] += l_0[j_2]
        layer += 1
        l_0 = l_1.copy()
        l_1 = l_2.copy()
    
    print(l_0[n-1])
