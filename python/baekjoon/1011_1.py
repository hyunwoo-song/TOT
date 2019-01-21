def warp(dist):
    minN = powN = maxN = warpCnt = 0; n =1
    while(1):
        powN = n*n
        minN = powN - n + 1
        maxN = powN + n
        if minN <= dist and dist <= maxN:
            if minN <= dist and dist <= powN:
                warpCnt = (n << 1) -1
            else:
                warpCnt = n<<1
            break
        n += 1
    return warpCnt

for i in range(int(input())):
    line = input().split()
    x = int(line[0]); y= int(line[1])
    dist = y - x
    print(warp(dist))