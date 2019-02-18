import sys

sys.stdin = open('input.txt', 'r')

N = 100

for t in range(1, 11):
    Arr = []
    sum_l = []

    T = int(input())
    sum_Arrz1 = 0
    sum_Arrz2 = 0
    for n in range(100):
        Arr.append(list(map(int, input().split())))

    for y in range(100):
        sum_Arry = 0
        sum_Arrx = 0
        for x in range(100):
            sum_Arry += Arr[y][x]
            sum_Arrx += Arr[x][y]
        sum_l.append(sum_Arry)
        sum_l.append(sum_Arrx)

    for z in range(100):
        sum_Arrz1 += Arr[z][z]
        sum_Arrz2 += Arr[z][99-z]
    sum_l.append(sum_Arrz1)
    sum_l.append(sum_Arrz2)
    max_l = max(sum_l)
    print(f'#{t} {max_l}')


