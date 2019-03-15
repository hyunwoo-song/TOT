import sys
sys.stdin = open('1463.txt', 'r')

def update(x,y):
    where = base + x -1
    IDT[where] = y
    where >>= 1

    while where:
        IDT[where] = IDT[where*2]+IDT[where*2+1]
        where >>= 1

def RSQ(ffrom, to):
    ffrom = ffrom +base -1
    to = to + base -1
    sum = 0
    while ffrom < to :
        if ffrom%2:
            sum += IDT[ffrom]
            ffrom += 1
        if not to%2:
            sum += IDT[to]
            to -=1
        ffrom >>= 1
        to >>= 1

    if ffrom == to:
        sum += IDT[ffrom]
    return sum





N,M,K = map(int, input().split())
howmany = N

base = 1
while base <= howmany:
    base <<=1

IDT = [0]*(base*2)

for now in range(base, howmany + base):
    IDT[now] = int(input())

for parent in range(base-1, 0, -1):
    IDT[parent] = IDT[parent*2]+IDT[parent*2+1]

for _ in range(N+2, N+M+K+2):
    a, b, c = map(int,input().split())

    if a == 1:
        update(b, c)
    elif a == 2:
        print(RSQ(b, c))



