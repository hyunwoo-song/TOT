import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용


def IsSafe(y, x):
    return y >= 0 and y < 5 and x >= 0 and x < 5 and _Arr[y][x] == 0


N = 5
for n in range(N):
    Arr =list(map(int, input().split()))

_Arr=[[0]*5 for _ in range(5)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]
val = 1
y = 0
x = 0
dir = 0
for n in range(25):
    _Arr[y][x] = val
    if not IsSafe(y+dy[dir], x+dx[dir]):
        dir += 1
        dir %= 4
    y += dy[dir]
    x += dx[dir]
    val += 1

print(_Arr)



