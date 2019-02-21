import sys
sys.stdin = open('input.txt', 'r')

def IsSafe(y, x):
    return y >= 0 and y < 100 and x >= 0 and x < 100 and Data[y][x]==1


T= 10

for _ in range(1,T+1):
    t= int(input())
    Data = []
    dy = [0, 0]
    dx = [-1, 1]
    dz = -1
    dir = 0
    y = 99
    x = 0
    for i in range(100):
        Data.append(list(map(int, input().split())))


    for n in range(100):
        if Data[99][n] == 2:
            new_x = n
            break

    while True:
        if not IsSafe(y + dy[dir], new_x + dx[dir]):
            dir += 1
            if dir // 2:
                dir %= 2
            if not IsSafe(y + dy[dir], new_x + dx[dir]):
                y -= 1
                dir = 0
        y += dy[dir]
        new_x += dx[dir]
        Data[y][new_x]= 2
        if y == 0:
            break
    print(new_x+1)


