import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용


def issafe(x,y) :
    return x >= 0 and x < 7 and y >= 0 and y < 7 and B[y][x] == 1

N = int(input())
B=[]
for n in range(N):
    B.append(list(map(int, input())))

dy=[-1,1,0,0]
dx=[0,0,-1,1]
me =2
for y in range(7):
    for x in range(7):
        life =49
        if B[y][x]:
            count = 1
            for dir in range(4):
                while life >0:
                    if issafe(x + dx[dir], y + dy[dir]):
                        x += dx[dir]
                        y += dy[dir]
                        if B[y][x]:
                            B[y][x] = me
                    life -= 1
print(B)

