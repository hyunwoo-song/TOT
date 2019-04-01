import sys
sys.stdin = open('1780.txt', )

def GS(y,x,size):
    z = Arr[y][x]
    for i in range(size):
        for j in range(size):
            if Arr[y+i][x+j] == z:

                if i == j == size-1:
                    Z[z-1] += 1
                else:
                    continue

            else:
                size //=3
                GS(y+i,x+j,size)
                return

N = int(input())
Arr = [list(map(int, input().split())) for n in range(N)]
Z=[0,0,0]

x=0
y=0

for i in range(N):
    for j in range(N):
        N //= 3
        GS(x+i*N, y+j*N, N)

