import sys
sys.stdin=open('5247.txt')

def CAL(x,y):
    global cnt

    if x < 0 or x-y>2*x:
        return

    while y != x:
        for i in range(4):
            if i == 0:
                x += 1
            elif i == 1:
                x -= 1
            elif i==2:
                x *= 2
            else:
                x -= 10
            cnt += 1
            CAL(x, y)



TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    cnt =0
    CAL(N,M)