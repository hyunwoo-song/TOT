import sys

sys.stdin = open('input.txt', 'r')

N = 5
Arr=[]
min = 0
arr= [[0]*5]*5
count=0

for n in range(N):
    Arr.append(list(map(int, input().split())))

while count < N:
    for y in range(5):
        for x in range(5):
            if min > Arr[y][x]:
                min = Arr[y][x]
                Arr[y][x] = 0x7FFFFFFF

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    for y in range(5):
        for x in range(5):
            Arr[y][x] = min
            while newX == N:
                for dir in range(4):
